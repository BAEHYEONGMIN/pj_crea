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


print('''
<html>
<head>
<title></title>
<meta charset = "utf-8">
<link rel="shortcut icon" href="img/KakaoTalk_20210101_210438090.ico"  />
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="color.js"> </script>
 </head>
<link rel="stylesheet" href="style.css">
<body>
<div class = "top">
<h1>

        <ul class="top_nav_menu2">
            <li>
                <div class = "top_nav_image">
                    <div>
                        <div class="main_img">
                            <strong>
                                <a href="Crea.py" class="saw"> <img src = "img/KakaoTalk_20201213_031432655.gif"  width=120px height=60px></a>
                            </strong>
                        </div main_img>

                        <div class="sub_title_p">
                            <div class="sub_title">
                                since 2015
                            </div sub_title>
                        </div>
                    </div>
                </div top_nav_image>
            </li>
            <li>
                <div class = "top_nav_title2">
                    <a class = "top_link" href = "Crea_sogae.py">CREA</a>
                </div top_nav_title2>
            </li>
            <li>
                <div class = "top_nav_title2">
                    <a class = "top_link" href = "게시판">게시판2</a>
                </div top_nav_title2>
            </li>
            <li>
                <div class = "top_nav_title2">
                    <a class = "top_link" href = "imsi.py">한줄 남기러가기</a>
                </div top_nav_title2>
            </li>
            <li>
                <div class = "top_nav_title_last2">
                    <a class = "top_link" href = "math_diary.py">두근두근수학일기</a>
                </div top_nav_title_last2>
            </li>
        </ul top_nav_menu2>

</h1>
</div top>

<div class="under_text" style = "height:auto;">
<div class="left_side">
<img src = "img/아이디어제보바람.png"  width=250px height=1000px>
</div left_side>
<div class="main_text">
    <div class="center">
    하루에 딱 30분씩 만드는 크레아 소개페이지<P>
    </div center>
</div main_text>
<div class="right_side">
<img src = "img/배형민.png"  width=250px height=1000px>
</div index>
</div right_side>
</body>
'''.format(update=getupdateLink(),delete=getdeletLink()))
