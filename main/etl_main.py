# This is the main class to Extract , Transform and Load to the Database

import sys
import json
from datetime import date
sys.path.append('..')
from connector.postgres_connector import PostgresConnector
from connector.sqs_connector import SQSConnector
from configuration import db_configuration,sqs_configuration,aws_configuration
from commons.masking import encrypt,decrypt

class ETL:
    """
    Initialize the ETL main class.

    Args:
    - sqs_configuration : to configure connection with SQS queue.
    - db_configuration : to configure connection with Postgres database.
    - aws_configuration : to configure connection with AWS

    Returns:
    None
    """
    def __init__(self, sqs_configuration, db_configuration, aws_configuration):
        self.sqs_conn = SQSConnector(sqs_configuration["SQS_ENDPOINT_URL"],sqs_configuration["SQS_QUEUE_NAME"],aws_configuration["AWS_ACCESS_KEY_ID"],aws_configuration["AWS_SECRET_ACCESS_KEY"])
        self.db_conn = PostgresConnector(db_configuration["POSTGRES_DATABASE"], db_configuration["POSTGRES_USER_NAME"], db_configuration["POSTGRES_PASSWORD"], db_configuration["POSTGRES_HOST"])

    def extract_message_from_sqs(self):
        """
        Retrieves a single message from the SQS queue.

        Returns:
        str: The message string
        """

        response = self.sqs_conn.receive_message()
        if response:
            message = response[0].get('Body')
            return message
        return None

    def transform_message(self, extracted_message):
        """
        Transform the message into required format for storage
        
        Args:
        - extracted_message (str): Extracted message

        Returns:
        str: transformed dictionary
        """
        extracted_message_json=json.loads(extracted_message)

        transformed_message = {
            "user_id" : extracted_message_json.get("user_id"),
            "device_type" : extracted_message_json.get("device_type"),
            "masked_ip" : encrypt(extracted_message_json.get("ip")), # Mask PII 
            "masked_device_id" : encrypt(extracted_message_json.get("device_id")), # Mask PII 
            "locale" : extracted_message_json.get("locale"),
            "app_version" : extracted_message_json.get("app_version"),
            "create_date" : str(date.today())
        }

        return transformed_message

    def load_message_to_database(self, message_data):
        """
        Loads the transformed message into the table "user_logins"
        
        Args:
        - message_data (str): Transformed message

        Returns:
        None
        """

        table="user_logins"
        columns=["user_id","device_type,masked_ip","masked_device_id","locale","app_version","create_date"]
        data_to_insert=[message_data.get("user_id"),message_data.get("device_type"),message_data.get("masked_ip"),message_data.get("masked_device_id"),message_data.get("locale"),message_data.get("app_version"),message_data.get("create_date")]
        self.db_conn.post(table,columns,data_to_insert)
    

    def process(self,number_of_messages_to_process):
        """
        Process ETL for any number of messages 
        Args:
        - number_of_messages_to_process (int): Number of message to process

        Returns:
        None
        """

        for i in range(number_of_messages_to_process):
            message = self.extract_message_from_sqs()
            if message:
                transformed_data = self.transform_message(message)
                self.load_message_to_database(transformed_data)
            
   

    def close(self):
        """
        Closes Postgres Connection
        """
        self.db_conn.close()

