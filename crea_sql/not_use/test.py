#!/usr/bin/python3
import os,pymysql
print("Content-Type: text/html")
print()


def getList():
    files = os.listdir('data')
    liststr=''
    for item in files:
        liststr = liststr + '<li><a href = "Crea.py?id={name}">{name}</a></li>'.format(name=item)
    return liststr

def make_board():
    connect = pymysql.connect(host='127.0.0.1', user='root', password='031415',
                   db='crea_db', charset='utf8')
    i=1
    str=''
    while i<2:
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        sql = "select * from imsi_sql where id ={num};".format(num = i)
        cursor.execute(sql)
        rows= cursor.fetchone()
        board_desc = rows["description"]
        board_id = rows["id"]
        board_date = rows["created"]
        str=str+'''
            <tr>
                <th>{id}</th>
                <th>{desc}</th>
                <th>{date}</th>
            </tr>
            '''.format(id=board_id,desc=board_desc,date=board_date)
        i=i+1
    cursor.close()
    return str
def get_auto_increment():
    connect = pymysql.connect(host='127.0.0.1', user='root', password='031415',
                   db='crea_db', charset='utf8')
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    sql = "show table status where name = 'imsi_sql';"
    cursor.execute(sql)
    rows= cursor.fetchone()
    return rows
max_num = get_auto_increment()
print(max_num)
