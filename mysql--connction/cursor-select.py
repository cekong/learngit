''''''
'''
https://www.imooc.com/video/9215
2-2 
https://www.imooc.com/video/9216
3-1
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

sql="select * from user"
cursor.execute(sql)
print(cursor.rowcount)

rs=cursor.fetchone()
print(rs)

rs=cursor.fetchmany(2)
print(rs)

rs=cursor.fetchall()
print(rs)


cursor.close()
conn.close()