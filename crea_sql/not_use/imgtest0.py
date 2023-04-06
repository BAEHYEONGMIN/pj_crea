#!/usr/bin/python3

import sys
import io
import pymysql
import base64
from io import BytesIO
import time
import cgi,pymysql
import PIL
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()

connect = pymysql.connect(host='127.0.0.1', user='root', password='031415',
                       db='crea_db', charset='utf8')

cursor = connect.cursor(pymysql.cursors.DictCursor)

sql = "select * from image where id = '8';"
cursor.execute(sql)
result = cursor.fetchone()
print(result['img_text'],end = '\n')
print(sys.getsizeof(result['img_text']),end = '\n')
decode_data = base64.b64decode(result['img_text'])
print(decode_data,end = '\n')
print(sys.getsizeof(decode_data))
# file2 = open('data/' + 'abc.jpg',"wb")
# file2.write(decode_data)
# file2.close()

cursor.close()
connect.close()
