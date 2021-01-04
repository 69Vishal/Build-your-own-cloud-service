# Building your own Cloud Service using python

This project is all about building your own cloud service With just an internet connection and a laptop using Python3 and MySQL
#
## Where do I start?
You should start by setting up your won server, you have a lot of option here either make your own server at home using Raspberry Pi 3 or 4(i recommend Raspberry pi 4 4GB variant) doing this you can have freedom of unlimited storage and you can set up in parallel as many as you want. If you want to do this for free then you can set up a server on Amazon AWS EC2 and install an ubuntu server on it.

## What do I do after setting up the server?
You have to update the system using `Sudo apt-get update` install Apache2, MySQL-server, Mysql-connector, and python3 on the server and you have to setup everything without error. Once you are doing this you can move forward editing `/etc/apache2/apache2.conf` and adding a line :
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
and run a simple command `sudo a2enmod cgi`, 
What this line of code does s that it enables CGI(Common Gateway Interface) in file `/var/www/Html/` and will allow us to smoothly run `.py` on our Apache Web Server, If you are still getting `Internal Server Error`, check `/var/log/apache2/error.log` file for errors.

## How do I set up my Web server?
Once you are done installing and setting up your server you have to upload all the files to  `/var/www/Html/` and change change permission so that anyone can execute through this command `$ sudo chmod 775 -R folder`(remove -R if you want to change permission for a single file and type your file name with extension where the folder is written). After doing all of this you can now start your server by typing `$ sudo service apache2 start` or `$ sudo service apache2 stop` if you want to stop your server.

## How do I set up MySQL?
Once everything above this line is working as it should and without error, you can now continue installing MySQL using through `$ Sudo apt-get install MySQL-server` and install and setup it using `$ sudo mysql_secure_installation`, once you are done setting up everything you can now access MySQL using `$ sudo MySQL -u user -p`(- u to define as which user you want to log in, -p to ask for user password before login) and after successful login, you have to create a new database named 'server' or if you want a custom name you can do it now `mysql> CREATE DATABASE server;` and your database will be created, now select that database using `mysql> USE server;`, now create a table called 'file' or anything you want `mysql> CREATE TABLE file(serial INT NOT NULL AUTO_INCREMENT PRIMARY KEY, access_id VARCHAR(6) NOT NULL, access_path VARCHAR(40) NOT NULL);`.

## How to connect my database with python?
Once you are done setting up the server and MySQL, Make sure you have installed MySQL.connector if not do it now by typing `$ sudo pip3 install mysql.connector` and then you have to edit `uploadrqst.py` and `downloadrqst.py` to change database login creds. open both files in a text editor or using nano `$ sudo nano /var/www/html/rqst/uploadrqst.py` and you find a line 
```db = MySQL.connector.connect(host='localhost', user='root', password='pass', database='server')```
change your database here if you have named it differently.

## Is client data safe?
No, this example is just for learning purposes and i don't think you will make a entire enterpise out of it. but to an extent it is secure, with just a line of in `.htacess` you can make it a bit secure so that if someone try to access the the folder where files are stored, server will deny to connect.


## Example
[Check out this Example](www.vishal.uno)
