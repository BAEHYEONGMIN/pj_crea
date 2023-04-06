
import os,pymysql


def getList():
    files = os.listdir('data')
    liststr=''
    for item in files:
        liststr = liststr + '<li><a href = "Crea.py?id={name}">{name}</a></li>'.format(name=item)
    return liststr




def get_row_num():
    connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                   db='crea_db', charset='utf8')
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT COUNT(*) FROM imsi_sql;"
    cursor.execute(sql)
    rows= cursor.fetchone()
    return rows['COUNT(*)']


def get_row_num_literary_contest():
    connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                   db='crea_db', charset='utf8')
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT COUNT(*) FROM crea_literary_contest;"
    cursor.execute(sql)
    rows= cursor.fetchone()
    return rows['COUNT(*)']


def make_board():
    max_num = get_row_num()
    connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                   db='crea_db', charset='utf8')
    i=1
    str=''
    while 0<max_num:
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        sql = "select * from imsi_sql where id ={num};".format(num = max_num)
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
        max_num=max_num-1
    cursor.close()
    return str


def make_board_literary_contest():
    max_num = get_row_num_literary_contest()
    connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                   db='crea_db', charset='utf8')
    i=1
    str=''
    while 0<max_num:
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        sql = "select * from crea_literary_contest where id ={num};".format(num = max_num)
        cursor.execute(sql)
        rows= cursor.fetchone()
        board_title = rows["title"]
        board_id = rows["id"]
        board_date = rows["created"]
        board_name = rows["name"]
        str=str+'''
            <tr>
                <th>{id}</th>
                <th><a class = 'title_black' href="literary_contest_click.py?title={title}">{title}</a></th>
		<th>{name}</th>
                <th>{date}</th>
            </tr>
            '''.format(id=board_id,title=board_title,name = board_name, date=board_date)
        max_num=max_num-1
    cursor.close()
    return str


def make_board_literary_contest_click(page):
    max_num = get_row_num_literary_contest()
    connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                   db='crea_db', charset='utf8')

    cursor = connect.cursor(pymysql.cursors.DictCursor)
    sql = "select * from crea_literary_contest where title ='{temp}';".format(temp=page)
    cursor.execute(sql)
    rows= cursor.fetchone()
    board_title = rows["title"]
    board_id = rows["id"]
    board_date = rows["created"]
    board_name = rows["name"]
    board_description = rows["description"]
    str='''
        <tr>
            <th>{id}</th>
            <th>{title}</th>
	    <th>{name}</th>
            <th>{date}</th>
        </tr>
        '''.format(id=board_id,title=board_title,name = board_name, date=board_date)
    cursor.close()
    return str
def make_board_literary_contest_description (page):
    max_num = get_row_num_literary_contest()
    connect = pymysql.connect(host='45.120.69.23', user='root', password='031415',
                   db='crea_db', charset='utf8')

    cursor = connect.cursor(pymysql.cursors.DictCursor)
    sql = "select * from crea_literary_contest where title ='{temp}';".format(temp=page)
    cursor.execute(sql)
    rows= cursor.fetchone()
    board_title = rows["title"]
    board_id = rows["id"]
    board_date = rows["created"]
    board_name = rows["name"]
    board_description = rows["description"]
    str='''    
    {description}
        '''.format(description = board_description)
    cursor.close()
    return str

