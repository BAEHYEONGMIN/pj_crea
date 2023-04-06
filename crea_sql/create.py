#!/usr/bin/python3
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()

import cgi,os
files = os.listdir('data')
liststr=''
for item in files:
    liststr = liststr + '<li><a href = "crea.py?id={name}">{name}</a></li>'.format(name=item)
form = cgi.FieldStorage()

if "id" in form:
    pageId=form.getvalue("id")
    description = open('data/'+pageId,'r', encoding='utf-8').read()
    update_link = '<a href="update.py?id={pageId}"></a>'.format(pageId=pageId)

else:
    pageId='MAIN'
    description='ㅎㅇ'
    update_link=''
if pageId=='MAIN':
    description='CREA'
print(pageId)


print('''
<html>
<head>
<title>{title}</title>
<meta charset = "utf-8">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="color.js"> </script>
 </head>
<link rel="stylesheet" href="style.css">
<body>
<h1><strong><a href="Crea.py" class="saw">CREA</a></strong>  <a href ="일지.html"> 일지</a>
 <input type="button" value="night" onclick="
NightDayHandler(this)
  ">
</h1>

<div class="under_text">
<ol>
 <div class="index">
  <a href ="Crea.py?id=MAIN" class="saw">   0.초기</a><p>
  <a href ="Crea.py?id=ORIGIN" class="saw"> 1.crea유래</a><p>
  <a href ="Crea.py?id=HISTORY" class="saw">2.crea연혁</a><p>
  3.음<p>
  <a href ="create.py"><input type="button" value = '추가하기'></a>
  {update}
</div>
</ol>
 <div class="main_text">
<div class="글쓰는데">
<form action="process_create.py"  method="post">
<p><input type = text name="title" placeholder="title"></p>
<p><textarea rows="4" name="description" placeholder="description"></textarea></p>
<p><input type = submit></p>
</form>
</div>
</div>
하루에 딱 30분씩 만드는 크레아 소개페이지<P>
</body>
'''.format(title=pageId,des=description,liststr=liststr,update=update_link))
