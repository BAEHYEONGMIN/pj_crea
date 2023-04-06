#!/usr/bin/python3
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()

import pymysql
import base64
from io import BytesIO
import time
import cgi
form = cgi.FieldStorage()
fileitem = form.getvalue('filename')
image=form.getvalue("image")
print(fileitem)
# bi_img = base64.b64encode(image)
# bi_img = bi_img.decode('UTF-8')
# title = 'testcase1'
# rating = '5'
# data = (title,bi_img,rating)
#
# connect = pymysql.connect(host='127.0.0.1', user='root', password='031415',
#                        db='crea_db', charset='utf8')
#
# cursor = connect.cursor(pymysql.cursors.DictCursor)
#
# sql = "insert into crea_math (title,text1,rating) values (%s,%s, %s);"
#
# cursor.execute(sql,data)
# connect.commit()
# sql = "select text1 from crea_math where id = 6;"
# cursor.execute(sql)
# rows= cursor.fetchone()
# result = base64.b64decode(rows['text1'])
# print(result)
# cursor.close()
# connect.close()
