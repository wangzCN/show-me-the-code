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

# link to Mysql
con = MySqlCon.Con()

for i in range(200):
    
    key = newKey()
    print(key)
    
    #insert to mysql
    MySqlCon.Insert(con, key)
    
MySqlCon.done(con)