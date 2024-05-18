import logging
import sys

from aws.dynamodb import insertData

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

try:
    magnitude = str(sys.argv[1]).replace("+", "強").replace("-", "弱")
    second = str(sys.argv[2])
    msg = "警告：台北地區預計震度" + magnitude + "級地震\n將於" + second + "秒後抵達"
    insertData(magnitude, second)

except ModuleNotFoundError:
    logging.error("=====錯誤:請確保request和sys module有被正確的安裝=====")

except IndexError:
    logging.error("=====錯誤:請確保呼叫此程式時參數有正確的引數(規模和秒數)=====")
