import sys
import json
from datetime import date

sys.path.append('..')

from connector.postgres_connector import PostgresConnector
from connector.sqs_connector import SQSConnector
from configuration import db_configuration,sqs_configuration,aws_configuration
from commons.masking import encrypt,decrypt
# Now you can use the os module to access environment variables

class ETL:
    def __init__(self, sqs_configuration, db_configuration, aws_configuration):
        self.sqs_conn = SQSConnector(sqs_configuration["SQS_ENDPOINT_URL"],sqs_configuration["SQS_QUEUE_NAME"],aws_configuration["AWS_ACCESS_KEY_ID"],aws_configuration["AWS_SECRET_ACCESS_KEY"])
        self.db_conn = PostgresConnector(db_configuration["POSTGRES_DATABASE"], db_configuration["POSTGRES_USER_NAME"], db_configuration["POSTGRES_PASSWORD"], db_configuration["POSTGRES_HOST"])

    def extract_message_from_sqs(self):
        # Retrieve a single message from the SQS queue
        response = self.sqs_conn.receive_message()
        if response:
            message = response[0].get('Body')
            return message
        return None

    def transform_message(self, extracted_message):
        # This is a dummy transform function. Customize as needed.
        print("extracted_message: ",extracted_message,type(extracted_message))
        extracted_message_json=json.loads(extracted_message)
        print("extracted_message_json: ",extracted_message_json,type(extracted_message_json))

        transformed_message = {
            "user_id" : extracted_message_json.get("user_id"),
            "device_type" : extracted_message_json.get("device_type"),
            "masked_ip" : encrypt(extracted_message_json.get("ip")),
            "masked_device_id" : encrypt(extracted_message_json.get("device_id")),
            "locale" : extracted_message_json.get("locale"),
            "app_version" : extracted_message_json.get("app_version"),
            "create_date" : str(date.today())
        }

        return transformed_message

    def load_message_to_database(self, message_data):
        table="user_logins"
        columns=["user_id","device_type,masked_ip","masked_device_id","locale","app_version","create_date"]
        data_to_insert=[message_data.get("user_id"),message_data.get("device_type"),message_data.get("masked_ip"),message_data.get("masked_device_id"),message_data.get("locale"),message_data.get("app_version"),message_data.get("create_date")]
        self.db_conn.post(table,columns,data_to_insert)
    

    def process(self,number_of_messages_to_process):
        for i in range(number_of_messages_to_process):
            message = self.extract_message_from_sqs()
            if message:
                transformed_data = self.transform_message(message)
                self.load_message_to_database(transformed_data)
            
   

    def close(self):
        self.db_conn.close()

