# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import xlwt
# import numpy as np
# workbook = xlwt.Workbook()
# worksheet = workbook.add_sheet('msj', cell_overwrite_ok=True)
# class FoodMsjPipeline(object):
#     def process_item(self, item, spider):
#         data = [item['foodname'], item['imgurl'], item['foodurl']]
#         data = np.transpose(data)
#         print(data)
#         print("-------------------------")
#         title = ('名称', '图片链接', '食物详情')
#         for i in range(0, 3):
#             worksheet.write(0, i, title[i])
#         row = 1
#         col = 0
#         for n, i, f in data:
#             worksheet.write(row, col, n)
#             col = col + 1
#             worksheet.write(row, col, i)
#             col = col + 1
#             worksheet.write(row, col, f)
#             col = 0
#             row = row + 1
#         workbook.save("msj.xls")
#         return item
import xlwt
import pymongo
from .settings import mongo_HOST, mongo_PORT, db_name, passWord, userName, collection_name
from scrapy.exceptions import DropItem

class FoodMsjPipeline(object):
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(mongo_HOST, mongo_PORT, connect=False)
        self.db = self.mongo_client[db_name]

        username = userName
        password = passWord
        if username and password:
            self.db.authenticate(username, password)
        self.collection = self.db[collection_name]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing{0}!'.format(data))
        if valid:
            count = len(item['foodname'])
            datalist = []
            for i in range(0, count):
                foodname = item['foodname'][i]
                imgurl = item['imgurl'][i]
                foodurl = item['foodurl'][i]
                data = {'foodname': foodname, 'imgurl': imgurl, 'foodurl': foodurl}
                datalist.append(data)
                self.collection.update_one({"foodname": data["foodname"]}, {"$set": data}, upsert=True)
        allRecordRes = self.collection.find()
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('msj', cell_overwrite_ok=True)
        row=0
        for record in allRecordRes:
            col=0
            row = row + 1
            for itemname in record:
                if itemname=='_id':
                    continue
                worksheet.write(0,col,itemname )
                worksheet.write(row, col, record[itemname])
                col=col+1
            workbook.save("msj.xls")
        return item
