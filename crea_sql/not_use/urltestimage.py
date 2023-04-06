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
print("hi")
import cgi,pymysql
form = cgi.FieldStorage()
image1=form.getvalue("image1")
image2.form.getvalue("image2")
image = image1 + image2
connect = pymysql.connect(host='127.0.0.1', user='root', password='031415',
                       db='crea_db', charset='utf8')

cursor = connect.cursor(pymysql.cursors.DictCursor)

sql = "insert into image (img_text) values(%s);"
cursor.execute(sql,image)
connect.commit()

cursor.close()
connect.close()
