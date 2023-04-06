#!/usr/bin/python3

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import cgi,pymysql
form = cgi.FieldStorage()
title=form.getvalue("title")
description=form.getvalue("content")
data = (title,content)
connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                       db='crea_db', charset='utf8')

cursor = connect.cursor()

sql = "insert into test (title,content) values(%s,%s);"
cursor.execute(sql,data)
connect.commit()

cursor.close()
connect.close()
