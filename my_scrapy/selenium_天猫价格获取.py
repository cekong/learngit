''''''
'''
https://coding.imooc.com/lesson/92.html#mid=3190
https://www.jianshu.com/p/6cc890328320
'''

from selenium import webdriver
from scrapy.selector import Selector


browser=webdriver.Firefox()
#天猫价格获取
browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.3.yYBVG6&id=538286972599&cm_id=140105335569ed55e27b&abbucket=15&sku_properties=10004:709990523;5919063:6536025")

t_selector = Selector(text=browser.page_source)
print (t_selector.css(".tm-price::text").extract())

# print (browser.page_source)
browser.quit()