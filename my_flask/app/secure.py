''''''
'''
配置文件

存放密码、账号等
存放生产环境与开发环境参数的值不同的参数

最好不要上传到git上
'''


DEBUG=True   #参数设置要大写
SQLALCHEMY_DATABASE_URI='mysql://root:password@127.0.0.1:3306/fisher'
                            #用于连接数据的数据库。
SQLALCHEMY_TRACK_MODIFICATIONS = False
                            #如果为true，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
                            #这需要额外的内存， 如果不必要的可以禁用它。

SECRET_KEY='7894561230123456789'


#email 配置
MAIL_SERVER='smtp.qq.com'
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USE_TSL=False
MAIL_USERNAME='55@qq.com'
MAIL_PASSWORD='tkvmdukmhvmrbgdj'
MAIL_SUBJECT_PREFIX='[鱼书]'
MAIL_SENDER='鱼书<hello@yushu.im>'

