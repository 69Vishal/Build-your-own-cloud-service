#!/usr/bin/python 
# -*- coding: UTF-8 -*-

# enable debugging
print("Content-Type: text/html\n\r\n")
print('''

<html>
<head>
    <link rel="stylesheet" href="css/py.css">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet">
    <link rel="icon" href="images/logo-for-meta.png">
    <title>Python test</title>
</head>
<body link='pink' vlink='pink' alink="white" >
<div class="main"><br>
<font size='50'>The69 Cloud Services</font>
<br>
<font color=white>File Access Station</font>
</div>
<br>
<div class='help'><font color=aqua>Wanna upload your files?</font> <a href='upload.py'>Click Here</a></div>
<br><br>
<div class='help'><font color='white' size='25'>Access Here</font></div>
<br>
<center>
<form action='rqst/downloadrqst.py' method='POST'>
<div class='help'><font color='aqua' style='font-size:25px;'>Enter Your 6 digit code</font></div>
<br>
<input type='text' name='rqst_id' minlength='6' maxlength='6' required>
<br><br>

<div class='help'>
<font color=silver>Doesn't understand what to do?</font> <a href='../help/access.txt'>Click Here</a>
<br>
</div>

<br>
<input type="image" name="submit" src="https://img.icons8.com/bubbles/100/000000/checked.png" alt="Submit" />
</form>
</center>

</body>
</html>

''')