#!/usr/bin/python3
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()

import cgi,os,module_test,pymysql
form = cgi.FieldStorage()
title =  form.getvalue("title")
body_string_center = '''
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
</tbody>
{board}
</table>
{description}


{body_right}
'''.format(body_left = body_string_left,body_center = body_string_center, body_right=body_string_right, page_id = title,board=module_test.make_board_literary_contest_click(title),description=module_test.make_board_literary_contest_description(title)))
