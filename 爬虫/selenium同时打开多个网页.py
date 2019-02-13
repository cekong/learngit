#_*_coding: utf-8_*_
from selenium import webdriver
import time
browser=webdriver.Firefox()
browser.get("https://www.zhihu.com/explore")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get("https://www.baidu.com")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[2])
browser.get("https://blog.csdn.net")
