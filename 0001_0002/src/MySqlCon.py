'''

@author: Wangz.cn
'''
import MySQLdb

def Con(host="localhost",user='root',passwd='0827',db='pyDB',port=3306):
    try:
        con = MySQLdb.connect(host,user,passwd,db,port)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return con

def CreTab(con):
    try:
        cur = con.cursor()
        cur.execute("creat table ActiveKey(key varchar(16))")
        con.commit()
        cur.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
def Insert(con,key):
    try:
        cur = con.cursor()
        cur.execute("insert into key_tab values(%s)",key)
        con.commit()
        cur.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        
def done(con):
    con.close()