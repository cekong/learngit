'''
控制chrome浏览器，访问百度，并搜索关键词Python，获取搜索结果
https://blog.csdn.net/qq_29186489/article/details/78661008
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()
#天猫价格获取
browser.get("https://www.baidu.com")
input=browser.find_element_by_id("kw")
input.send_keys("Python")
input.send_keys(Keys.ENTER)
wait=WebDriverWait(browser,10)
wait.until(EC.presence_of_element_located((By.ID,"content_left")))
print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
time.sleep(10)
browser.close()


