import pymongo
import csv


mongo_HOST = "localhost"
mongo_PORT = 27017
db_name = "mydb"
collection_name ="mydata"
userName = None
passWord = None

mongo_client = pymongo.MongoClient(mongo_HOST, mongo_PORT, connect=False)
db = mongo_client[db_name] #连接db_name数据库，没有则自动创建

username = userName
password = passWord

if username and password:
    db.authenticate(username, password)
collection = db[collection_name]#使用collection_name集合，没有则自动创建

with open('result.csv', 'w', newline='') as csvfileWriter:
    writer = csv.writer(csvfileWriter)
    fieldList=['name', 'age']
    writer.writerow(fieldList)
    allRecordRes = collection.find()
    # 写入多行数据
    for record in allRecordRes:
        print(f"record = {record}")
        recordValueLst = []
        for field in fieldList:
            if field not in record:
                recordValueLst.append("None")
            else:
                recordValueLst.append(record[field])
        try:
            writer.writerow(recordValueLst)
        except Exception as e:
            print(f"write csv exception. e = {e}")