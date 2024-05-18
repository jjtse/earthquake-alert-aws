from datetime import datetime
import logging
import boto3

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# 創建 DynamoDB 客户端
dynamodb = boto3.client('dynamodb')

# insert data
def insertData(magnitude, second):
    localDateTime = datetime.now().strftime('%Y%m%d%H%M%S')

    try:
        response = dynamodb.put_item(
            TableName='Earthquake_Alarm',
            Item={
                'id': {'S': localDateTime},  # 項目: {'字串属性':'內容'}
                'area': {'S': 'Taipei'},
                'level': {'S': magnitude} ,
                'countdown': {'S': second}
            }
        )
        logging.info("Data inserted successfully!")
    except Exception as e:
        logging.error(f"Error: {e}")


# get item by key
def getItem():
    try:
        response = dynamodb.get_item(
            TableName='Earthquake_Alarm',
            Key={
                'id': {'S': '20240505021428'}
            }
        )

        item = response.get('Item')
        if item:
            logging.info(item)
        else:
            logging.info("Item not found.")

    except Exception as e:
        logging.error(f"Error: {e}")