#!/usr/bin/python3

import sys,json
import io
import pymysql
import base64
from io import BytesIO
import time
import cgi,pymysql
from PIL import Image
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()
data = {}
with open("../img/crea_math.png", "br") as file:
        img = file.read()
print(img, end="\n===")
data['img'] = base64.encodebytes(img)
print("=====####=====")
data['img']=data['img'].decode("utf-8")
# print(json.dumps(data))
print(data['img'])
print("==!!===")
# print(data['img'])
print("=@@==")
decode_data = base64.b64decode(data['img'])
print(decode_data)
#
# file2 = open('data/' + 'test.jpg',"wb")
# file2.write(decode_data)
# file2.close()
#
#
# connect = pymysql.connect(host='127.0.0.1', user='root', password='031415',
#                        db='crea_db', charset='utf8')
#
# cursor = connect.cursor(pymysql.cursors.DictCursor)
#
# sql = "insert into image (img_text) values(%s)"
# cursor.execute(sql,data['img'])
# connect.commit()
#
# cursor.close()
# connect.close()
# print("finish")
