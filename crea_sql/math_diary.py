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

i=0

f = open("/var/www/html/crea_sql/body_left", 'r', encoding = 'utf-8')
body_string_left = f.read()
f.close()
f = open("/var/www/html/crea_sql/body_right", 'r', encoding = 'utf-8')
body_string_right = f.read()
f.close()


body_string_center = '''
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <a id = "download" href="data/app-release-v6.zip"><생각 쓰레기통 어플(시험판)></a>
        <br></br>

        <form action="process_math.py" method="post" enctype="multipart/form-data">
            Upload File : (사진은 현재 지원하지 않습니다.)<input type = "file" name = "filename" /><P>
            title       : <input type = "text" name = "title" placeholder="제목"/></p><p>
            name      : <input type = text name = "name" placeholder="이름 "/></p><p>
            conet     : <p><textarea rows="2" style="width:80%;" name="text1" placeholder="내용적어주세요"></textarea></p><p>
            <input type="submit">
        </form>
    </body>
</html>

'''
print('''
{body_left}
{body_center}
</tbody>
</table>

{body_right}
'''.format(body_left = body_string_left,body_center = body_string_center, body_right=body_string_right,title=get_title_description.pageId,liststr=module_test.getList(),update=getupdateLink(),delete=getdeletLink()))

