import os
from dotenv import load_dotenv
import sys
from pathlib import Path
sys.path.append('..')
load_dotenv(dotenv_path=Path('..') / '.env')

sqs_configuration = {
    "SQS_ENDPOINT_URL" : os.getenv("SQS_ENDPOINT_URL"),
    "SQS_QUEUE_NAME" : os.getenv("SQS_QUEUE_NAME")
}

aws_configuration = {
    "AWS_ACCESS_KEY_ID" : os.getenv("AWS_ACCESS_KEY_ID"),
    "AWS_SECRET_ACCESS_KEY" : os.getenv("AWS_SECRET_ACCESS_KEY")
}
db_configuration = {
    'POSTGRES_HOST': os.getenv("POSTGRES_HOST"),
    'POSTGRES_USER_NAME': os.getenv("POSTGRES_USER_NAME"),
    'POSTGRES_PASSWORD': os.getenv("POSTGRES_PASSWORD"),
    'POSTGRES_DATABASE': os.getenv("POSTGRES_DATABASE")
}
