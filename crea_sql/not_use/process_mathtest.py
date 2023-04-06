#!/usr/bin/python3

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("Content-Type: text/html")
print()
import cgi,pymysql
form = cgi.FieldStorage()
filename = form.getvalue("filename")
title=form.getvalue("title")
rating=form.getvalue("rating")
content=form.getvalue("content")

print(title)
print("." + rating)
# file = open('data/' + title+'.jpg',"wb")
# file.write(filename)
# file.close()
