#!/usr/bin/python3

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import cgi,pymysql
form = cgi.FieldStorage()
connect = pymysql.connect(host='45.120.69.23', user='root', password='031415', db='crea_db', charset='utf8')
cursor = connect.cursor(pymysql.cursors.DictCursor)
if "id" in form:
    pageId=form.getvalue("id")
    sql = "select * from imsi_sql where title=%s;"
    cursor.execute(sql,pageId)
    result = cursor.fetchone()
    description = result['description']

    cursor.close()
    connect.close()
    # description = description.replace('<','&lt;')
    # description = description.replace('>','&gt;')
else:
    pageId='Welcome'
    description='CREA'
