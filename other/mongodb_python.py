import pymongo

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

'''插入数据'''
collection.insert({"name":"wangwu","age":19})#插入一条数据
# users=[{"name":"wangwu","age":19},{"name":"lisi","age":20}]#插入多条
# collection.insert(users)

'''查询全部'''
for i in collection.find():
    print(i)
print('-1-------------------------------------------')

'''更新数据'''
collection.update({"name":"zhangsan"},{'$set':{"age":20}})

'''查询name=zhangsan的数据'''
for i in collection.find({"name":"zhangsan"}):
    print(i)
print('-2-------------------------------------------')

'''删除name=zhangsan的全部记录'''
collection.remove({'name': 'zhangsan'})

'''#删除name=wangwu的某个id的记录'''
id = collection.find_one({"name":"wangwu"})["_id"]
collection.remove(id)
'''查询全部'''
for i in collection.find():
    print(i)
print('-3-------------------------------------------')

'''对数据进行排序,其中 1 为升序，-1为降序'''
for i in collection.find().sort([("age",1)]):
    print(i)
print('-4-------------------------------------------')

'''
#limit()方法用来读取指定数量的数据
#skip()方法用来跳过指定数量的数据
#下面表示跳过1条数据后读取3条
'''
for i in collection.find().skip(1).limit(3):
    print(i)
print('-5-------------------------------------------')

'''找出age是19,18的数据'''
for i in collection.find({"age":{"$in":(19,18)}}):
    print(i)
print('-6-------------------------------------------')


'''找出age是19或18的记录'''
for i in collection.find({"$or":[{"age":18},{"age":19}]}):
    print(i)