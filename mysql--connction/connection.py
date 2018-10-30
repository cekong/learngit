''''''
'''
https://www.imooc.com/video/9214
2-1 Python-数据库连接对象 connection 
'''


import MySQLdb
print(MySQLdb)
conn=MySQLdb.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='password',
    db='wbdatabase',
    charset='utf8'
)

cursor=conn.cursor()
print(conn)
print(cursor)
cursor.close()
conn.close()