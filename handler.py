import os
import boto3
import logging
import json
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

REGION = os.getenv("REGION")
TABLE_NAME = 'dh-events'

resource = boto3.resource('dynamodb', region_name=REGION)
table = resource.Table(TABLE_NAME)


def lambda_handler(event, context):
    store_records(event['Records'])

    response = {
        'statusCode': 200,
        'body': 'successfully stored records',
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    return response


def store_records(records):
    try:
        with table.batch_writer() as writer:
            for record in records:
                event = json.loads(record['body'])
                writer.put_item(Item=event)
    except ClientError as err:
        logger.error("Failed to store records into table %s. Reason: %s, %s", TABLE_NAME,
                     err.response['Error']['Code'], err.response['Error']['Message'])
        raise
