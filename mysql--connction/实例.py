''''''
'''
https://www.imooc.com/video/9219
转账小程序：一人给另一人转账100元

'''

import sys
import MySQLdb

class TransferMoney(object):
    def __init__(self,conn):
        self.conn=conn

    def check_acct_available(self,accid):
        cursor=self.conn.cursor()
        try:
            sql="select * from account where acctid=%s"%accid
            cursor.execute(sql)
            print("check_acct_available",sql)
            rs=cursor.fetchall()
            if len(rs)!=1:
                raise Exception("帐号不存在",accid)
        finally:
            cursor.close()


    def has_enough_money(self,accid,money):
        cursor=self.conn.cursor()
        try:
            sql="select * from account where acctid=%s and money>=%s"%(accid,money)
            cursor.execute(sql)
            print("has_enough_money",sql)
            rs=cursor.fetchall()
            if len(rs)!=1:
                raise Exception("帐号没有足够的钱",accid)
        finally:
            cursor.close()


    def reduce_money(self,accid,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" %(money,accid)
            cursor.execute(sql)
            print("reduce_money", sql)
            if cursor.rowcount != 1:
                raise Exception("帐号减款失败",accid)
        finally:
            cursor.close()


    def add_money(self,accid,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" %(money,accid)
            cursor.execute(sql)
            print("reduce_money", sql)
            if cursor.rowcount != 1:
                raise Exception("帐号加款失败",accid)
        finally:
            cursor.close()


    def transfer(self,source_accid,target_accid,money):
        try:
            self.check_acct_available(source_accid)
            self.check_acct_available(target_accid)
            self.has_enough_money(source_accid,money)
            self.reduce_money(source_accid,money)
            self.add_money(target_accid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e



if __name__=='__main__':
    source_accid=sys.argv[1]
    target_accid=sys.argv[2]
    money=sys.argv[3]

    conn = MySQLdb.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='password',
        db='wbdatabase',
        charset='utf8'
    )
    trans_money=TransferMoney(conn)

    try:
        trans_money.transfer(source_accid,target_accid,money)
    except Exception as e:
        print("错误：",e)
    finally:
        conn.close()
