#!/usr/bin/python3

import sys
import io
import cgi,pymysql

form = cgi.FieldStorage()
filename = form.getvalue("filename")
data = (filename)

connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                       db='crea_db', charset='utf8')

cursor = connect.cursor()


sql = "insert into img_test (image) values(%s);"
cursor.execute(sql,data)
connect.commit()

cursor.close()
connect.close()
print("Location: img_test_html.py")
print()
