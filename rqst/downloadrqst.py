#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

# enable debugging
print("Content-Type: text/html\n\r\n")
import os
import cgi, cgitb
from os import path
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='pass', database='server')
form = cgi.FieldStorage()
rqst_id = form['rqst_id'].value
try:
    cursor = db.cursor()
    rqst = "select access_path from file where access_key = '{}';".format(rqst_id)
    cursor.execute(rqst)
    result = cursor.fetchone()
    suf = result[0]
    final_path = '../client_data/' + suf
    show_link = True
except:
    link = "<font color=silver>We couldn't fetch your file from 6 digit code <b><font color=aqua>{}</font></b> given by you, </font> <a href='../access.py' >Try again</a>" .format(rqst_id)
    show_link =False
if show_link:
    link = "<font color=silver>Your file is ready for downloading, </font> <a href='{}' target='_blank' download>Click Here to Download.</a>".format(final_path)
else:
    link = "<font color=silver>We couldn't fetch your file from 6 digit code <b><font color=aqua>{}</font></b> given by you, </font> <a href='../access.py' >Try again</a>" .format(rqst_id)
print(f'''

<html>
<head>
    <link rel="stylesheet" href="../css/py.css">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet">
    <link rel="icon" href="../images/logo-for-meta.png">
    <title>Python test</title>
</head>
<body link='pink' vlink='pink' alink="white" >
<div class="main"><br>
<font size='50'>The69 Cloud Services</font>
<br>
<font color=white>File Download Station</font>
</div>
<br>
<div class='help'>
{link}
<br>
</div>

</body>
</html>

''')
# Code by 69vishal
