#!/usr/bin/python3

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()

import cgi,os,module_test
form = cgi.FieldStorage()

if "id" in form:
    pageId=form["id"].value
    description = open('data/'+pageId,'r',encoding='utf-8').read()
    description = description.replace('<','&lt;')
    description = description.replace('>','&gt;')
else:
    pageId='Welcome'
    description='CREA'

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
            <input type = "submit" value = "삭제하기">
        '''
    else:
        delete_action= ''
    return delete_action

f = open("/var/www/html/crea_sql/body_test", 'r', encoding = 'utf-8')
body_string = f.read()
f.close()



print('''
{body}
'''.format(body = body_string))
