''''''
'''
https://coding.imooc.com/lesson/92.html#mid=3190
https://www.jianshu.com/p/6cc890328320
'''

from selenium import webdriver
from scrapy.selector import Selector


browser=webdriver.Firefox()
#知乎登录
browser.get("https://www.zhihu.com/signin")

browser.find_element_by_css_selector(".SignFlow-accountInput input").send_keys("***")
browser.find_element_by_css_selector(".SignFlow-password input").send_keys("**")
browser.find_element_by_css_selector(".SignFlow-submitButton").click()

