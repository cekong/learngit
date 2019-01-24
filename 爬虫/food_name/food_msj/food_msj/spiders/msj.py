# -*- coding: utf-8 -*-
import scrapy
from food_name.food_msj.food_msj.items import FoodMsjItem

class MsjSpider(scrapy.Spider):
    name = 'msj'
    allowed_domains = ['meishij.net/chufang/diy/']
    start_urls = ['http://meishij.net/chufang/diy/']

    def parse(self, response):
        item = FoodMsjItem()
        item['foodname'] = response.xpath('//div[@id="listtyle1_list"]/div/a/img/@alt').extract()
        item['imgurl'] = response.xpath('//div[@id="listtyle1_list"]/div/a/img/@src').extract()
        item['foodurl'] = response.xpath('//div[@id="listtyle1_list"]/div/a/@href').extract()
        yield item
