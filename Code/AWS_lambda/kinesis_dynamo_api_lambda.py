import json
import boto3

def lambda_handler(event, context):
    print("Event received:")
    print(event)

    method = event['context']['http-method']

    if method == "GET":
        dynamo_client = boto3.client('dynamodb')
        customer_id = event['params']['querystring']['CustomerID']

        response = dynamo_client.get_item(
            TableName='Customers',
            Key={'CustomerID': {'N': customer_id}}
        )

        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Item', {}))
        }

    elif method == "POST":
        record = event['body-json']
        record_string = json.dumps(record)

        kinesis_client = boto3.client('kinesis')
        kinesis_client.put_record(
            StreamName='APIData',
            Data=record_string,
            PartitionKey='string'
        )

        return {
            'statusCode': 200,
            'body': json.dumps(record)
        }

    return {
        'statusCode': 501,
        'body': json.dumps("Unsupported HTTP method")
    }
