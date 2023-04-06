#!/usr/bin/python3
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("Content-Type: text/html")
print()

import json

import cgi,pymysql
string = ''
string_created = ''
i='99'
connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                       db='crea_db', charset='utf8')
print('{"status":"OK", "articles": [')
# sql = "select * from crea_math where id = %s;"
while(int(i)>0):
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT EXISTS (select * from crea_math where id = %s) AS flag;"
    cursor.execute(sql,i)
    rows = cursor.fetchone()
    if rows['flag']==1:
        sql = 'select id,title,text1,text2 from crea_math where id = %s;'
        cursor.execute(sql,i)
        rows = cursor.fetchone()
        sql = 'select created from crea_math where id = %s;'
        cursor.execute(sql,i)
        rows_created = cursor.fetchone()
        string_created = str(rows_created['created'])
        rows['created'] = string_created
        string = json.dumps(rows)
        print(string, end='')
        print(', ')
        # print(string)

    i = int(i)-1
    i = str(i)
print(']}')
cursor.close()
connect.close()
