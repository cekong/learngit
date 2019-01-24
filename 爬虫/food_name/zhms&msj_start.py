# -*- coding: utf-8 -*-
from food_name.food_zhms.food_zhms.spiders.zhms import ZhmsSpider
from food_name.food_msj.food_msj.spiders.msj import MsjSpider
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import tkinter
import tkinter.messagebox
from scrapy.settings import Settings
from scrapy.crawler import CrawlerRunner

keyword=input("请输入要查询的网站(中华美食网/美食杰):")

if keyword=="中华美食网":
    settings = Settings({
        'SPIDER_MODULES': ['food_zhms.food_zhms.spiders.zhms'],
        'ROBOTSTXT_OBEY': True,
        # 启用pipelines组件
        'ITEM_PIPELINES': {
            'food_zhms.food_zhms.pipelines.FoodZhmsPipeline': 300, },
        'CONCURRENT_REQUESTS': 1

    })
    runner = CrawlerRunner(settings)
    d = runner.crawl('zhms')
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
elif keyword=="美食杰":
    settings = Settings({
        'SPIDER_MODULES': ['food_msj.food_msj.spiders.msj'],
        'ROBOTSTXT_OBEY': True,
        # 启用pipelines组件
        'ITEM_PIPELINES': {
            'food_msj.food_msj.pipelines.FoodMsjPipeline': 299, },
        'CONCURRENT_REQUESTS': 1

    })
    runner = CrawlerRunner(settings)
    d = runner.crawl('msj')
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
else:
    tkinter.messagebox.showinfo('提示', '请输入要查询的网站： 中华美食网/美食杰')


