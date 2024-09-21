from chromedriver_py import binary_path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd


def pre_order(account_string, password_string):
    # 创建Chrome驱动实例
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    wait = WebDriverWait(driver, 120)

    ehURL="https://e-hentai.org/"
    driver.get(ehURL)
    time.sleep(4)
    login_button = wait.until(EC.element_to_be_clickable(
        driver.find_element(By.XPATH, '//*[@id="nb"]/div[6]/a')))
    login_button.click()
    # 登录
    account = driver.find_element(By.XPATH, '/html/body/div/form/table/tbody/tr[1]/td[2]/input')
    account.send_keys(account_string)
    time.sleep(2)
    password = driver.find_element(By.XPATH, '/html/body/div/form/table/tbody/tr[2]/td[2]/input')
    password.send_keys(password_string)
    time.sleep(2)
    login_button = driver.find_element(By.XPATH, '/html/body/div/form/table/tbody/tr[3]/td/input')
    login_button.click()
    time.sleep(4)

    exURL = "https://exhentai.org/"
    # 打开网页
    driver.get(exURL)
    time.sleep(4)

    file_path = 'favorTable.txt'
    favor_urls = pd.read_csv(file_path, sep='\t', header=None)
    favor_urls.columns = ['URL', 'XPath']

    for favor_url in favor_urls.itertuples():
        driver.get(getattr(favor_url, 'URL'))
        time.sleep(1)

        try:
            add_favorite_button = driver.find_element(By.XPATH, '/html/body/div/form/div/div[2]/div/input[1]')
            if add_favorite_button:
                favor_num = driver.find_element(By.XPATH, getattr(favor_url, 'XPath'))
                favor_num.click()
                time.sleep(0.1)
                add_favorite_button.click()
                time.sleep(0.5)
        except:
            continue


if __name__ == '__main__':
    pre_order("yourAccount", "yourPassword")
