# Building your own Cloud Service using python

This project is all about Building your own cloud service With just an internet connection and a laptop using Python3 and MySQL

## Where do I start?
You should start by setting up your won sserver, you have a lot of option here either make your own server at home using Raspberry Pi 3 or 4(i recommend Raspberry pi 4 4gb varient) doing this you can have freedom of unlimited storage and you can setup in parellel as many as you want. If you want to do this for free then you can setup a server on Amazon AWS EC2 and install ubuntu server on it.

## What do I do after setting up server?
You have to update the system using `Sudo apt-get update` install Apache2, MySQL-server, Mysql-connector, and python3 on the server and you have to setup everyhing without error. Once you are doing doing this you can move forward editing `/etc/apache2/apache2.conf` and adding a line :
```
<Directory /var/www/html>
  Options +ExecCGI
  AddHandler cgi-script .py
</Directory>
```
you have to enter this line after 
```
<Directory /var/www/>
	Options Indexes FollowSymLinks
	AllowOverride None
	Require all granted
</Directory>
```
What this line of code does s that it enables CGI(Comman Gateway Interface) in file `/var/www/html/` and will allow us to smoothly run `.py` on our Apache Web Server, If you are still getting `Internal Server Error`, check `/var/log/apache2/error.log` file for errors.
## How do I set up my Web server?
Once you are done indtalling and setting up your server you have to upload all the files to  `/var/www/html/` and chnage change permission so that anyone can execute through this command `$ sudo chmod 775 -R folder`(remove -R if you want to change permission for a single file and type your file name with extension ehre filder is written)		
