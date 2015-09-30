# WINDOWS 10
# python 2.7.10
# Eclipse with pyDev
# mysql-5.6.26-winx64
'''

@author: Wangz.cn
'''
import random
import MySqlCon
import MySQLdb 

def newKey(length = 16):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    str =''
    str_len = len(chars)-1;
    for i in range(0,length):
        str += chars[random.randint(0, str_len)]
    return str

con = MySqlCon.Con()

for i in range(200):
    
    key = newKey()
    print(key)
    MySqlCon.Insert(con, key)
    
MySqlCon.done(con)
        