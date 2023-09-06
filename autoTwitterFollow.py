import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import chromedriver_binary


TWITTER_BASE = "https://twitter.com/"
LOGIN_ID = ""
LOGIN_USER_NAME = ""
PASSWORD = ""
ACCOUNTLISTFILE = ""

if __name__ == "__main__":
    # Driver
    driver = get_driver()
    # ログイン
    login_flg = do_login(driver)
    # フォロー
    login_flg = do_follow(driver)

    driver.quit()
    
def get_driver():
    #　ヘッドレスモードでブラウザを起動
    options = Options()
    driver = webdriver.Chrome()
    return driver

# twitterログイン
def do_login(driver):
    # ログインURL
    login_url = TWITTER_BASE + "login"
    driver.get(login_url)
    time.sleep(2)

    # アカウント入力
    element_account = driver.find_element(By.NAME,"text")
    element_account.send_keys(LOGIN_ID)
    time.sleep(2)

    # 次へボタンクリック
    element_login = driver.find_element(by=By.XPATH,value= '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
    element_login.click()
    time.sleep(2)

    # パスワード入力
    print(driver.current_url)
    element_pass = driver.find_element(By.NAME,"password")
    element_pass.send_keys(PASSWORD)
    time.sleep(2)

    # ログインボタンクリック
    element_login = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
    element_login.click()
    time.sleep(2)

def do_follow(driver):
    # ファイルを開いて行ごとに読み込み、配列に格納
    lines = []
    with open(ACCOUNTLISTFILE, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())  # 行末の改行文字を取り除いて格納

    # ログインボタン押下
    for line in lines:
        driver.get(str(line))
        time.sleep(2)
        # ログインボタンクリック
        element_follow = driver.find_elements(By.CSS_SELECTOR, '.css-901oao.r-1awozwy.r-jwli3a.r-6koalj.r-18u37iz.r-16y2uox.r-37j5jr.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0 > .css-901oao.css-16my406.css-1hf3ou5.r-poiln3.r-a023e6.r-rjixqe.r-bcqeeo.r-qvutc0 > .css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
        element_follow[0].click()