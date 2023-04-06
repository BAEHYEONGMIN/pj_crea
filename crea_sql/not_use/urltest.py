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
import cgi,pymysql
form = cgi.FieldStorage()
image=form.getvalue("image")
title=form.getvalue("title")
text1=form.getvalue("text1")
data=(title,text1)
connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                       db='crea_db', charset='utf8')

cursor = connect.cursor(pymysql.cursors.DictCursor)

sql = "insert into crea_math (title, text1) values(%s,%s)"
cursor.execute(sql,data)
connect.commit()

cursor.close()
connect.close()
