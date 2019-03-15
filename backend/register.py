#!/usr/bin/env python3
import cgi
import sqlite3
#import tkinter
print("Content-type:text/html\r\n\r\n")
form=cgi.FieldStorage()
uname=form.getvalue('username')
pswd1=form.getvalue('password')
pswd2 = form.getvalue('pswd')

conn = sqlite3.connect('../cgi-bin/logindetails.db')

#cur=conn.execute("SELECT * FROM LOG2")

if pswd1==pswd2:
    conn.execute('INSERT INTO LOGIN1 VALUES(?,?);',(uname,pswd1))
    #conn.execute("INSERT INTO LOG2 VALUES(" + '"' + uname + '"' + ',' + '"' + pswd1 + '"' + ")")
    conn.commit()
    print('<html>')
    print("<body background='../images.jpeg'>")
    print("<h1><marquee>Thank You for signing up!</marquee></h1>")
    print("<form action='/ludotemplate.html'>")
    print('<br/><br/><br/><br/><br/><br/><br/><br/><br/><center><input type="Submit" style="width:18em; height:8em; font-size:2em" value="Go to Login Page"/></center>')
    print('</form>')
    print('</body></html>')
    
else:
    print('<html>')
    print("<body background='../images.jpeg'>")
    print("<form action='/ludotemplate.html'>")
    print('<br/><br/><br/><br/><br/><br/><br/><br/><br/><center><input type="Submit" style="width:24em; height:8em; font-size:2em" value="Passwords do not match, click to try again"/></center>')
    print('</form>')
    print('</body></html>')
