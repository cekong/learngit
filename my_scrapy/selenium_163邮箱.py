from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui
driver = webdriver.Firefox()
url = "http://mail.163.com/"
wait = ui.WebDriverWait(driver,10)
driver.get(url)
time.sleep(5)

#跳转到登陆frame
frame= driver.find_element_by_id('mainBg').find_element_by_class_name('loginWrap').find_element_by_id('loginDiv').find_element_by_css_selector('iframe')
driver.switch_to.frame(frame)

time.sleep(5)

#登陆邮箱
your_mail=''
your_pwd=''

driver.find_element_by_name("email").send_keys(your_mail)
driver.find_element_by_name("password").send_keys(your_pwd)
time.sleep(3)


driver.find_element_by_id("dologin").click()
time.sleep(6)
driver.quit()
print("login in")


