import time, os, re
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests as req

# 使用 Chrome 的 WebDriver
my_service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome()
files = []

def get_taiko_info():

    try:
    # 走訪網址
        driver.get("https://faithcreation.jp/taikonotatsujin/entry/")
        wait = WebDriverWait(driver, 10)

        #找到'新着順'就往下一步
        order_button = wait.until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, '新着順')
                )
        )
        #按一下按鈕
        order_button.click()
        #找到分頁按鈕就往下一步
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.pageFeed-nav._on")
                )
        )

        sleep(5)

        #所有data-audiofilename元素的陣列、真正audio存放網址
        media_url = "https://faithcreation.jp/taikonotatsujin/media/entries/"
        global files

        #有1~10頁
        for page in range(1, 11):
            items = driver.find_elements(By.CSS_SELECTOR, "li.entrylist-item.animation")

            #寫入files
            for item in items:
                entry_name = item.find_element(By.CSS_SELECTOR, "div.entry_name").text
                entry_author = item.find_element(By.CSS_SELECTOR, "span.entry_authorname").text

                entry = {"artist": entry_author,
                        "title": entry_name,
                        "url": f"{media_url}" + item.get_attribute("data-audiofilename")
                    }
                files.append(entry)
            
            try:
                #找到下一頁按鈕
                next_page = wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, f"a.pageFeed-navBt[data-href='{page + 1}']")
                    )
                )
                next_page.click()

                #刷新頁面
                sleep(3)

                #繼續抓
                wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, "li.entrylist-item.animation")
                    )
                )
            except Exception as e:
                print("最底頁了")
                print("=" * 50)
                break

        #根據entry no.排序
        files = sorted(files, key=lambda d: d['url'])
    except TimeoutException:
        print("try use a longer sleep time")
    finally:
        driver.quit()

def download():
    if not os.path.isdir("testOutput"):
        os.mkdir("testOutput") #doesn't exist then create

    global files

    for file in range(0, len(files)): #index 0~498
        res = req.get(files[file]['url'])
        if res.status_code == 200:
            #跳脫字元處理
            processed_artist = files[file]['artist'] = re.sub(r'[\\/*?:"<>|]', "", files[file]['artist'])
            processed_title = files[file]['title'] = re.sub(r'[\\/*?:"<>|]', "", files[file]['title'])

            #載過的跳過，沒載過的就下載
            if not os.path.isfile(f"testOutput/{processed_artist}_-_{processed_title}.mp3"):
                with open(f"testOutput/{processed_artist}_-_{processed_title}.mp3", "wb") as o:
                    o.write(res.content)
                    print(f"downloaded file({file+1}):", f"{files[file]['artist']} - {files[file]['title']}")
                    sleep(1)

    
if __name__ == "__main__":
    start = time.time()

    get_taiko_info()
    download()

    end = time.time()
    print("下載完成，共耗時:", round(end - start, 2), "秒")
