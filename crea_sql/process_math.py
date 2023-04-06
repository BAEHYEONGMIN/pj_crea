#!/usr/bin/python3

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import cgi,pymysql
form = cgi.FieldStorage()
filename = form.getvalue("filename")
title=form.getvalue("title")
name = form.getvalue("name")
text1=form.getvalue("text1")

data = (title,text1,name)
connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                       db='crea_db', charset='utf8')

cursor = connect.cursor()


sql = "insert into crea_math (title,text1,text2,created) values(%s,  %s,%s,now());"
cursor.execute(sql,data)
connect.commit()

cursor.close()
connect.close()
print("Location: crea.py")
print()
