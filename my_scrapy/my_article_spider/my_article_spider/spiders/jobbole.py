# -*- coding: utf-8 -*-

''''''
'''
https://coding.imooc.com/learn/list/92.html
https://git.imooc.com/coding-92/coding-92/src/master

xpath选择器  &&  css选择器

extract_first() == .extract()[0]


scrapy startproject 项目名
scrapy genspider 爬虫名字 爬虫的网址 / scrapy genspider -t 模板名字 爬虫名字 爬虫的网址
启动爬虫: scrapy crawl 爬虫名字/scrapy runspider 爬虫文件名称
'''

import scrapy
import re
from scrapy.http import Request
from my_article_spider.items import MyArticleItem
from my_article_spider.utils.common import get_md5
import datetime
from scrapy.loader import ItemLoader

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']



    '''---------------------------------'''
    '''试用xpath选择器和css选择器'''
    # start_urls = ['http://python.jobbole.com/89331/']
    #
    # def parse(self, response):
    #     ''''''
    #     '''xpath选择器'''
    #     title=response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1/text()').extract()
    #     print(title)
    #     create_date=response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·","").strip()
    #     print(date)
    #     zanshu=response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0]
    #     zanshu=re.match(".*(\d+).*",zanshu).group(1)
    #     pinglun=response.xpath("//a[@href='#article-comment']/span")
    #     content=response.xpath("//div[@class='entry']").extract()[0]
    #     taglist=response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
    #     tag = ",".join(taglist)
    #
    #     '''css选择器'''
    #     title=response.css(".entry-header h1::text").extract()[0]
    #     create_date=response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·","").strip()
    #     zanshu=response.css(".vote-post-up h10::text").extract_first()
    #     pinglun=response.css(".hide-on-480::text").extract()
    #     content=response.css(".entry").extract()[0]
    #     taglist = response.css(".entry-meta-hide-on-mobile a::text").extract()
    #     tag = ",".join(taglist)
    #     pass
    '''---------------------------------'''
    start_urls = ['http://blog.jobbole.com/all-posts/']
    def parse(self, response):
        ''''''
        '''
        1.获取文章列表页中的文章url并交给scrapy，下载后并进行解析
        2.获取下一页的URL并交给scrapy进行下载，下载完成后交给parse函数
        '''
        #解析列表页中的所有url
        post_nodes=response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url=post_node.css("img::attr(src)").extract_first("")
            post_url=post_node.css("::attr(href)").extract_first("")
            yield Request(url=post_url,meta={"front_image_url":image_url},callback=self.parse_detail)

        # #获取下一页的URL并交给scrapy进行下载
        # next_urls=response.css(".next.page-numbers::attr(href)").extract_first("")
        # if next_urls:
        #     yield Request(url=next_urls, callback=self.parse)




    def parse_detail(self, response):
        # article_item=MyArticleItem()
        # title = response.css(".entry-header h1::text").extract()[0]
        # create_date=response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·","").strip()
        # try:
        #     create_date=datetime.datetime.strptime(create_date, "%Y/%m/%d").date()
        # except Exception as e:
        #     create_date = datetime.datetime.now().date()
        # zanshu=response.css(".vote-post-up h10::text").extract_first()
        # front_image_url=response.meta.get("front_image_url","")#封面图
        # article_item["title"]=title
        # article_item["create_date"] =create_date
        # article_item["zanshu"] =zanshu
        # article_item["front_image_url"] =[front_image_url]
        # article_item["url_id"]=get_md5(response.url)

        # 通过item loader加载item
        front_image_url = response.meta.get("front_image_url", "")# 文章封面图
        item_loader = ItemLoader(item=MyArticleItem(), response=response)
        item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_value("url_id", get_md5(response.url))
        item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("front_image_url", [front_image_url])
        item_loader.add_css("zanshu", ".vote-post-up h10::text")
        #调用这个方法来对规则进行解析生成item对象
        article_item = item_loader.load_item()


        yield article_item
