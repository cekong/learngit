# -*- coding: utf-8 -*-
import scrapy
from food_name.food_zhms.food_zhms.items import FoodZhmsItem

class ZhmsSpider(scrapy.Spider):
    name = 'zhms'
    allowed_domains = ['zhms.cn/cp/']
    start_urls = ['http://zhms.cn/cp/']

    def parse(self, response):
        item = FoodZhmsItem()
        item['foodname'] = response.xpath('//div[@class="fl w930"]/ul/li/a/img/@alt').extract()
        item['imgurl'] = response.xpath('//div[@class="fl w930"]/ul/li/a/img/@src').extract()
        item['foodurl'] = response.xpath('//div[@class="fl w930"]/ul/li/a/@href').extract()
        yield item