''''''
'''
模型层
https://coding.imooc.com/lesson/194.html#mid=12779  4-8 定义第一个模型类

sqlalchemy 
Flask_SQLAlchemy

SQLAlchemy 是Python 社区最知名的 ORM 工具之一，为高效和高性能的数据库访问设计，
实现了完整的企业级持久模型。

ORM(对象关系映射)将数据库中的表与面向对象语言中的类建立了一种对应关系。
'''
from sqlalchemy import Column,Integer,String,Time

from app.models.base import db,Base


#用代码创建数据表
class Book(Base):
    id=Column(Integer,primary_key=True,autoincrement=True)
                                        #autoincrement自增长
    title=Column(String(50),nullable=False)#nullable设置此值不为空
    author=Column(String(30),default='佚名')#当此值为空时，默认设置为佚名
    binding = Column(String(20))
    publisher=Column(String(50))
    price=Column(String(30))
    pages=Column(Integer)
    pubdate=Column(String(20))
    isbn = Column(String(15),nullable=False,unique=True)#unique此值唯一，不能重复
    summary=Column(String(1000))
    image=Column(String(50))
    image = Column(String(50))
    #MVC M Model 只有数据
    #ORM 对象关系映射 


    def sample(self):
        pass