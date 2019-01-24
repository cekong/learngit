# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodZhmsItem(scrapy.Item):
    foodname = scrapy.Field()
    imgurl = scrapy.Field()
    foodurl = scrapy.Field()
