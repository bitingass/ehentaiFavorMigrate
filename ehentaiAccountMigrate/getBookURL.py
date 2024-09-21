import time
import pandas as pd
from chromedriver_py import binary_path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def pre_order(account_string, password_string):
    book_urls = []
    book_tags = []

    URL = "https://e-hentai.org/"
    # 创建Chrome驱动实例
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)

    # 设置等待时间
    wait = WebDriverWait(driver, 120)

    # 打开网页
    driver.get(URL)

    time.sleep(4)

    login_button = wait.until(EC.element_to_be_clickable(
        driver.find_element(By.XPATH, '//*[@id="nb"]/div[6]/a')))

    # time.sleep(6)
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

    favorite_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/a')
    favorite_button.click()
    time.sleep(2)

    # get all the book's url and tag

    while True:
        try:
            next_page_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[5]/a')
        except:
            print("没有找到下一页按钮，获取当前页信息并结束循环")
            for i in range(1, 51):
                try:
                    book_url = driver.find_element(By.XPATH,
                                                   f'/html/body/div[2]/form/div/div[{i}]/div[2]/a').get_attribute(
                        "href")
                    # time.sleep(2)
                    book_urls.append(book_url)
                    book_tag = driver.find_element(By.XPATH,
                                                   f'/html/body/div[2]/form/div/div[{i}]/div[4]/div[1]/div[1]')
                    time.sleep(2)
                    book_tags.append(book_tag.text)
                except:
                    break
            break

        time.sleep(0.9)

        for i in range(1, 51):
            book_url = driver.find_element(By.XPATH,
                                           f'/html/body/div[2]/form/div/div[{i}]/div[2]/a').get_attribute("href")
            # time.sleep(0.5)
            book_urls.append(book_url)
            book_tag = driver.find_element(By.XPATH,
                                           f'/html/body/div[2]/form/div/div[{i}]/div[4]/div[1]/div[1]')
            # time.sleep(0.5)
            book_tags.append(book_tag.text)
        print("该页完成记录")

        if next_page_button.is_enabled():
            next_page_button.click()
            time.sleep(0.9)
        else:
            break

    # 保存数据到txt文件
    data = {
        "url": book_urls,
        "tag": book_tags
    }

    df = pd.DataFrame(data)

    # 输出 DataFrame，查看数据结构
    print(df)

    # 将 DataFrame 保存为 txt 文件，每行保存 url 和 tag
    with open("ehentaiURL.txt", "w") as f:
        for index, row in df.iterrows():
            f.write(f"{row['url']}\t{row['tag']}\n")

    print("数据已成功写入 ehentaiURL.txt 文件")


if __name__ == '__main__':
    pre_order("yourAccount", "yourPassword")
