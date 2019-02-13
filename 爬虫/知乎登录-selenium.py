from selenium import webdriver
from scrapy.selector import Selector
browser = webdriver.Firefox()
#知乎模拟登陆
browser.get("https://www.zhihu.com/signup")
signup_switch_bt = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span')
#如果内容显示登录，则证明在注册页面，需要点击一下切换到登录页面
if signup_switch_bt.text == '登录':
    signup_switch_bt.click()
#找到填写用户名的输入框
uname_textfield = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input')
#找到填写密码的输入框
pwd_textfield = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input')
#找到登录按钮
signup_bt = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button')
#填写用户名，需要替换为你的用户名
uname_textfield.send_keys('user_name')
#填写密码，需要替换为你的密码
pwd_textfield.send_keys('your_passwd')
#点击登录
signup_bt.click()