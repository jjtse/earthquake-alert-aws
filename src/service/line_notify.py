import logging
import requests

lineUrl = "https://notify-api.line.me/api/notify"
lineToken = "您的金鑰"


def lineWebhook(msg) -> None:
    headers = {"Authorization": "Bearer " + lineToken}
    data = {'message': msg}
    try:
        response = requests.post(lineUrl, headers=headers, data=data)
        response.raise_for_status()  # 抛出 HTTP 請求異常
        logging.info('Line Notify 發送成功')

    except requests.exceptions.HTTPError as e:
        logging.error('Line Notify API 回應錯誤: %s', e)
        logging.error('錯誤訊息: %s', response.json())
