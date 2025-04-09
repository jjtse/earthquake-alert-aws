import logging

from aws.dynamodb import insertData
from service.line_notify import lineWebhook

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

try:
    msg = "警告：台北地區預將發生3級以上地震"
    insertData()
    lineWebhook(msg)

except Exception as e:
    logging.error("系統發生錯誤: %s", e)