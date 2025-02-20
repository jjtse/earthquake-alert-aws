# earthquake-alert-aws
**Building an Earthquake Alert Service with AWS DynamoDB and Lambda**  

ref. [brianoy/EEW_line_notify](https://github.com/brianoy/EEW_line_notify)  
download. [地牛Wake up](https://eew.earthquake.tw/)  

## Line Message API
因Line Notify於2025/3/31終止服務，調整使用MessageAPI，將訊息發送給自己
* Push message: One-to-one
* Message Type: [Document](https://developers.line.biz/en/reference/messaging-api/#text-message)

```shell
curl -v -X POST https://api.line.me/v2/bot/message/multicast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "to": ["U4af4980629...","U0c229f96c4..."],
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        },
        {
            "type":"text",
            "text":"Hello, world2"
        }
    ]
}'
```

## IAM 角色權限
使用者、使用者群組 AmazonDynamoDBFullAccess，或自行設定DynamoDB的存取政策

## DynamoDB
「全託管」意味着AWS負責管理和維護服務的所有方面，包括基礎設施、硬件、軟件、安全性和性能等。對於用戶來說，只需要使用服務的功能，而不需要擔心或參與底層基礎設施的管理。

### Policy 許可權
```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "AllDynamodb",
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::475794918554:user/Devloper"
			},
			"Action": [
				"dynamodb:*"
			],
			"Resource": [
				"arn:aws:dynamodb:ap-northeast-1:475794918554:table/Earthquake_Alarm"
			]
		}
	]
}
```

## 開發Python應用程式
安裝AWS Python SDK: Boto3 >>> `pip install boto3`

```python
# 創建 DynamoDB 客户端
dynamodb = boto3.client('dynamodb')

# 向 DynamoDB 表中插入數據
def insertData(magnitude, second):

    try:
        # 插入數據
        response = dynamodb.put_item(
            TableName='Your Table Name',
            Item={
                '欄位': {'字串属性': '內容'},
                '欄位': {'字串属性': '內容'},
                '欄位': {'字串属性': '內容'} ,
                '欄位': {'字串属性': '內容'}
            }
        )
        logging.info("Data inserted successfully!")
    except Exception as e:
        logging.error(f"Error inserting data: {e}")

```
