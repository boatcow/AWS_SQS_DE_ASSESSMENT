import boto3

class SQSConnector:

    def __init__(self, endpoint_url,queue_name, aws_access_key_id=None, aws_secret_access_key=None):
        self.queue_name = queue_name
        self.endpoint_url=endpoint_url
        self.client = boto3.client(
            'sqs',
            region_name='us-west-2',
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            verify=False
        )

    def send_message(self, message_body):
        response = self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message_body
        )
        return response['MessageId']

    def receive_message(self, max_messages=1, wait_time_seconds=1):
        response = self.client.receive_message(
            QueueUrl=self.endpoint_url+'/'+self.queue_name,
            MaxNumberOfMessages=max_messages,
            WaitTimeSeconds=wait_time_seconds
        )
        return response.get('Messages', [])

    def delete_message(self, receipt_handle):
        self.client.delete_message(
            QueueUrl=self.queue_url,
            ReceiptHandle=receipt_handle
        )
