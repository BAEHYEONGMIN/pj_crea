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
이벤트페이지(진)<p></P>
<div event>
<a class = "event" href="event_literary_contest.py" class="saw"> <img src = "img/event_description_literary_contest.png"  width=100% height=600px center></a>
</div event>

제목) 제 1회 크레아배 신춘문예.<p></p>  <p>
내용 ) 신춘문예입니다.<p></p> <p>
양식 : 자유입니다. 크레아로 삼행시같은거 가능합니다.<p>
일시 : 2021.11.19~(종료일자 미정)<p>
참여방법 : 아래링크에서 입력하심 됩니다.<p></p> <p>
<a href="literary_contest.py" class ="saw" style="color : red;"> <작성 링크></a><p>

상품)<p>
1등: 치킨<p>
2등: 집<p>
후원)권형록<p>
주의사항)><p>
작성한 게시물의 저작권은 서비스 제공자에게 양도됩니다.<p>
공란으로 제출하면 에러납니다.<P>
<hr width = "99%" color = "black">
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
</table>

{body_right}
'''.format(body_left = body_string_left,body_center = body_string_center, body_right=body_string_right,str=module_test.make_board_literary_contest(),title=get_title_description.pageId,liststr=module_test.getList(),update=getupdateLink(),delete=getdeletLink()))
