# This file provides a Python class (SQSConnector) that acts as a wrapper around
# the boto3 library to interact with AWS Simple Queue Service (SQS). The class
# allows for sending, receiving, and deleting messages from an SQS queue.

import boto3

class SQSConnector:
    """
    Initialize the SQSConnector class.

    Args:
    - endpoint_url (str): The endpoint URL for the SQS queue.
    - queue_name (str): The name of the SQS queue.
    - aws_access_key_id (str, optional): AWS access key. Defaults to None.
    - aws_secret_access_key (str, optional): AWS secret access key. Defaults to None.

    Returns:
    None
    """
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
        """
        Send a message to the SQS queue.

        Args:
        - message_body (str): The content of the message.

        Returns:
        str: The message ID of the sent message.
        """
        response = self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message_body
        )
        return response['MessageId']

    def receive_message(self, max_messages=1, wait_time_seconds=1):
        """
        Receive messages from the SQS queue.

        Args:
        - max_messages (int, optional): Maximum number of messages to retrieve. Defaults to 1.
        - wait_time_seconds (int, optional): The duration (in seconds) the call will wait for a message to arrive 
          in the queue before returning. Defaults to 1.

        Returns:
        list: A list of messages from the SQS queue.
        """
        response = self.client.receive_message(
            QueueUrl=self.endpoint_url+'/'+self.queue_name,
            MaxNumberOfMessages=max_messages,
            WaitTimeSeconds=wait_time_seconds
        )
        return response.get('Messages', [])

    def delete_message(self, receipt_handle):
        """
        Delete a message from the SQS queue using its receipt handle.

        Args:
        - receipt_handle (str): The receipt handle of the message to delete.

        Returns:
        None
        """
        self.client.delete_message(
            QueueUrl=self.queue_url,
            ReceiptHandle=receipt_handle
        )
