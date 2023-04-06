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
<form action="process_imsi.py"  method="post">
<textarea rows = "2" cols = "100"placeholder = "글적어요", style ="width: 80%;" name = "description"></textarea>
<input type = submit></p>
</form><p>

<table class = "table" border = "1" width="90%">
<colgroup>
<col width = "5%">
<col width = "80%">
<col width = "55%">
</colgroup>
 <thead>
 <tr>
     <th>번호</th>
     <th>내용</th>
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
</body>
{body_right}
'''.format(body_left = body_string_left,body_center = body_string_center, body_right=body_string_right,str=module_test.make_board(),title=get_title_description.pageId,liststr=module_test.getList(),update=getupdateLink(),delete=getdeletLink()))
