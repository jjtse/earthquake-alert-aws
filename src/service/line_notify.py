import logging
import requests
import json

lineUrl = "https://api.line.me/v2/bot/message/push"
lineToken = "你的Message api金鑰"


def lineWebhook(msg) -> None:
    headers = {"Authorization": "Bearer " + lineToken, 'Content-Type':'application/json'}
    data = {
            'to':'one-to-one user id',
            'messages':[{
            'type': 'text',
            'text': "台北地區$ " + msg,
            "emojis": [
            {
              "index": 0,
              "productId": "5ac21a18040ab15980c9b43e",
              "emojiId": "048"
            }]
        }]
    }
    try:
        response = requests.post(lineUrl, headers=headers, data=json.dumps(data).encode('utf-8'))
        response.raise_for_status()  # 抛出 HTTP 請求異常
        logging.info('Line Notify 發送成功')

    except requests.exceptions.HTTPError as e:
        logging.error('Line Notify API 回應錯誤: %s', e)
        logging.error('錯誤訊息: %s', response.json())