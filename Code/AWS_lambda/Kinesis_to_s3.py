from __future__ import print_function

import base64
import boto3
from datetime import datetime

s3_client = boto3.client('s3')
timestamp_str = datetime.now().strftime("%d-%b-%Y-%H%M%S")
kinesis_records = []

def lambda_handler(event, _):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        kinesis_records.append(payload)

    content = '\n'.join(kinesis_records)
    s3_key = f'output-{timestamp_str}.txt'

    s3_client.put_object(Body=content, Bucket='aws-de-project', Key=s3_key)

    return f'Successfully processed {len(event["Records"])} records.'
