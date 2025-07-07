import json
import base64
import boto3
from datetime import datetime

def lambda_handler(event, _):
    client = boto3.client('dynamodb')

    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        string_record = payload.decode('utf-8')
        data = json.loads(string_record)

        # Create customer row
        customer_key = {'CustomerID': {"N": str(data['CustomerID'])}}
        customer_attrs = {
            str(data['InvoiceNo']): {
                'Value': {"S": "Some overview JSON for the UI goes here"},
                'Action': "PUT"
            }
        }
        client.update_item(TableName='Customers', Key=customer_key, AttributeUpdates=customer_attrs)

        # Create inventory row
        inventory_key = {'InvoiceNo': {"N": str(data['InvoiceNo'])}}

        stock_data = dict(data)
        stock_data.pop('InvoiceNo', None)
        stock_data.pop('StockCode', None)
        stock_json = json.dumps(stock_data)

        inventory_attrs = {
            str(data['StockCode']): {
                'Value': {"S": stock_json},
                'Action': "PUT"
            }
        }
        client.update_item(TableName='Invoices', Key=inventory_key, AttributeUpdates=inventory_attrs)

    return f"Successfully processed {len(event['Records'])} records."
