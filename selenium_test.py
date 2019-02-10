import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import threading
import time
import copy

# リクエスト数
NUM_REQUEST = 10
# 現在使っておらず
random_talk = []
# URL
url = "http://localhost:8080"

# テストクラス
class RequestTest():
    def __init__(self):
        pass
    def make_driver(self):
        # 流しっぱなし
        while True:
            print('start')
            driver = webdriver.Chrome(options=Options().add_argument('--headless'))
            driver.get(url)
            iframe = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'id-hogehoge')))
            # iframe使うような奴は遷移させる
            driver.switch_to_frame(iframe)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'a'))).click()
                time.sleep(10)
            driver.quit()
            print('stop')

if __name__ == "__main__":
    list_class = []
    for d in range(NUM_REQUEST):
        list_class.append(RequestTest())
        thread = threading.Thread(target=list_class[d].make_driver)
        thread.start()
