''''''
'''
用于调试scrapy

或者在cmd中用scrapy shell 爬虫的网址 用于调试

https://www.jianshu.com/p/395591050986
https://git.imooc.com/coding-92/coding-92/src/master/ArticleSpider

倒立验证码： https://github.com/muchrooms/zheye
'''

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))#文件所在目录
print(os.path.dirname(os.path.abspath(__file__)))#文件所在文件夹的目录

# execute(["scrapy","crawl","jobbole"])
execute(["scrapy","crawl","zhihu"])