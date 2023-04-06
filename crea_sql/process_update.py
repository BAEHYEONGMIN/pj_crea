#!/usr/bin/python3

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


import cgi,os
form = cgi.FieldStorage()
pageId=form["pageId"].value
title=form["title"].value
description=form['description'].value

opened_file = open('data/'+ pageId, 'w', encoding = 'utf-8')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId,'data/'+title)

print("Location: Crea.py?id="+title)
print()
