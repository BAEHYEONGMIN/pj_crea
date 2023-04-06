#!/usr/bin/python3
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()

import cgi,os,module_test,get_title_description,pymysql
form = cgi.FieldStorage()

def getupdateLink():
    if "id" in form:
        update_link ='update.py?id={}'.format(get_title_description.pageId)
    else:
        update_link=''
    return update_link

def getdeletLink(): #링크는 아니에요
    if "id" in form:
        delete_action='''
            <form action="process_delete.py" method="post">
            <input type = "hidden" name = "pageId"  value="{}">
            <input type = "submit" value = "삭제하기">
        '''.format(get_title_description.pageId)
    else:
        delete_action= ''
    return delete_action


body_string_center = '''
<form action="process_literary_contest.py" method="post" enctype="multipart/form-data">
            제목       : <input type = "text" name = "title" placeholder="제목"/></p><p>
            작성자      : <input type = text name = "name" placeholder="이름 "/></p><p>
            내용    : <p><textarea rows="2" style="width:80%;" name="description" placeholder="내용적어주세요"></textarea></p><p>
            <input type="submit">
        </form>
<p>

<table class = "table" border = "1" width="90%">
<colgroup>
<col width = "5%">
<col width = "60%">
<col width = "10%">
<col width = "25%">
</colgroup>
 <thead>
 <tr>
     <th>번호</th>
     <th>제목</th>
	<th>작성자</th>
     <th>시간</th>
 </tr>
 </thead>
 <tbody>
'''

i=0

f = open("/var/www/html/crea_sql/body_left", 'r', encoding = 'utf-8')
body_string_left = f.read()
f.close()
f = open("/var/www/html/crea_sql/body_right", 'r', encoding = 'utf-8')
body_string_right = f.read()
f.close()



print('''
{body_left}
{body_center}
 {str}
</tbody>
</table>

{body_right}
'''.format(body_left = body_string_left,body_center = body_string_center, body_right=body_string_right,str=module_test.make_board_literary_contest(),title=get_title_description.pageId,liststr=module_test.getList(),update=getupdateLink(),delete=getdeletLink()))
