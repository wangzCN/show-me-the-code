#Windows 10
#python 2.7.10
#eclipse with pydev
#redis 2.8 for windows
'''

@author: Wangz.cn
'''
import random
import redis

def newKey(length = 16):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    str =''
    str_len = len(chars)-1;
    for i in range(0,length):
        str += chars[random.randint(0, str_len)]
    return str

red_con = redis.Redis(host="localhost",port = 6379 ,db = 0)

for i in range(200):
    activekey = newKey()
    key_id = i;
    print(activekey)
    red_con.set(key_id,activekey)
