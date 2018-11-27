from selenium import webdriver
import time


browser=webdriver.Firefox()
#知乎登录
browser.get("https://www.imooc.com/")
#等待页面网页加载完成
time.sleep(3)
#定位实战tab
tab=browser.find_element_by_xpath('/html/body/div[1]/div/ul/li[3]/a')
#点击
tab.click()
#等待页面加载完
time.sleep(3)
#断言文案“后端开发”显示了
content=browser.find_element_by_xpath('/html/body/div[3]/div/a[4]')
assert u"后端开发" in content.text
#退出
browser.quit()