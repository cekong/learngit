''''''
'''
https://www.imooc.com/video/9217
3-2 
'''


import MySQLdb

conn=MySQLdb.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='password',
    db='wbdatabase',
    charset='utf8'
)

cursor=conn.cursor()

sql_insert="insert into user(userid,username) values(7,'name7')"
sql_update="update user set username='name11' where userid=1"
sql_delete="delete from user where userd=2"
try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)

    conn.commit()##提交数据
except Exception as e:
    print(e)
    conn.rollback()

cursor.close()
conn.close()