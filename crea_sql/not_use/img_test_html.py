#!/usr/bin/python3

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("Content-Type: text/html")
print()

import cgi,os,pymysql
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
print('''
<html>
<head>
<title></title>
<meta charset = "utf-8">
<link rel="shortcut icon" href="../img/KakaoTalk_20210101_210438090.ico"  />
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="color.js"> </script>
 </head>
<link rel="stylesheet" href="../style.css">
<body>
<div class = "top">
<h1>
    <div class="main_img">
        <strong>
            <a href="crea.py" class="saw"> <img src = "../img/KakaoTalk_20201213_031432655.gif"  width=200px height=100px></a>
        </strong>
    </div main_img>
    <p class="sub_title_p">
    <div class="sub_title">
        since 2015
    </div sub_title>
        <input type="button" value="night" onclick="NightDayHandler(this)">
    <div class ="top_nav">
        <ul class="top_nav_menu">
            <li>
                <div class = "top_nav_title">
                    <a class = "top_link" href = "crea_sogae.py">CREA</a>
                </div top_nav_title>
            </li>
            <li>
                <div class = "top_nav_title">
                    <a class = "top_link" href = "luckynumber.py">행운의 숫자</a>
                </div top_nav_title>
            </li>
            <li>
                <div class = "top_nav_title">
                    <a class = "top_link" href = "imsi.py">낙서</a>
                </div top_nav_title>
            </li>
            <li>
                <div class = "top_nav_title_last">
                    <a class = "top_link" href = "math_diary.py">앱</a>
                </div top_nav_title_last>
            </li>
        </ul top_nav_menu>
    </div top_nav>
</h1>

</div top>

<div class="under_text" style = "height:auto;">
<div class="left_side">
<img src = "../img/아이디어제보바람.png"  width=250px height=1000px>
</div left_side>

<div class="main_text">
<div class="center">
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form action="img_test.py" method="post" enctype="multipart/form-data">
            Upload File : <input type = "file" name = "filename" /><P>
            title       : <input type = "text" name = "title" placeholder="제목?"/></p><p>
            name      : <input type = text name = "name" placeholder="이름 "/></p><p>
            conet     : <p><textarea rows="2" style="width:80%;" name="text1" placeholder="내용적어주세요"></textarea></p><p>
            <input type="submit">
        </form>
    </body>
</html>
</div center>
</div main_text>
<div class="right_side">
<img src = "../img/배형민.png"  width=250px height=1000px>
</div right_side>

'''.format())
