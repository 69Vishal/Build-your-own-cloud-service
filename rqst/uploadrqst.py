#!/usr/bin/python3.8
print("Content-Type: text/html\n\r\n")
import os
import cgi, cgitb
import shutil
import random
import string
import os.path
import mysql.connector 
addr = '../data/'
#creates a token
def token_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

token = token_generator(6)
#connect to Database
db = mysql.connector.connect(host='localhost', user='root', password='Vishal@19', database='server')
def update_db(final_path):
    global token
    command = "INSERT INTO file(access_key, access_path) VALUES('{}', '{}');".format(token, final_path)             
    cursor = db.cursor()
    cursor.execute(command)
    db.commit()
#saves file to server
form = cgi.FieldStorage()
filedata = form['upload']
if filedata.filename:
    fn = os.path.basename(filedata.filename)
    extension = os.path.splitext(fn)[1][0:]
    newfile = token + extension
    open(fn, 'wb').write(filedata.file.read())
    os.rename(fn, newfile)
    shutil.move(newfile, addr)
    final_dest = newfile
    update_db(final_dest)
    message = 'File uploaded & encrypted successfully'
else:
    message = 'File was not uploaded successfully'


print(f'''

<html>
<head>
    <link rel="stylesheet" href="../css/py.css">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet">
    <link rel="icon" href="../images/logo-for-meta.png">
    <title>Python test</title>
</head>
<body link='pink' vlink='pink' alink="white">
<div class="main"><br>
<font size='50'>The69 Cloud Services</font>
<br>
<font color=white>File Upload Station</font>
</div>
<br>
<div class='token_show'><font color='#dc93ff'>
{message}<br><br> Your token ID is <b><font color='aqua'>{token}</font></b>
</div>
<br><br>
<div class='help'><font color='silver'>
Please keep this token ID secure without this token ID no one can access yout file(not even us)
</div>
<br>
<div class='help'><font color=aqua>Wanna access your files?</font> <a href='../access.py'>Click Here</a></div>
</body>
</html>

''') 