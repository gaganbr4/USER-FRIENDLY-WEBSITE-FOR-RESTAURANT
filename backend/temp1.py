#!/usr/bin/env python3
import cgi
import sqlite3
#from tkinter import messagebox


conn=sqlite3.connect('/var/www/cgi-bin/logindetails.db')
print("Content-type:text/html\r\n\r\n")
#conn.execute("CREATE TABLE LOGIN1(USERNAME TEXT, PASSWORD TEXT)")
#conn.execute("INSERT INTO LOG2 VALUES('adarsh','ada')")
#conn.commit()
#conn.execute("INSERT INTO LOG2 VALUES('akarsh','aka')")
#conn.commit()


form=cgi.FieldStorage()
uname=form.getvalue('username')
password=form.getvalue('password')
#uname='adarsh'
#password='ada'
cur=conn.execute("SELECT * FROM LOGIN1;")
# To print a String stored in variable with double quotes we need to use '"'+variablename+'"'
flag=0


for row in cur:
    if row[0]==uname:
        if row[1]==password:
            print('<html>')
            print("<body background='../images.jpeg'>")
            print('<head><title>loginpagebttn</title></head>')
            print('<form action="/Ludo-game.html">')
            print('<br/><br/><br/><br/><br/><br/><br/><br/><br/><center><input type="submit" style="width:22em; height:8em; font-size:2em" value="PLAY GAME"/></center>')
            print("</form> </html>")
            flag=1
            break
        else:
            #messagebox.showinfo('Re','Passwords do not match. Re-type passwords')
            #print("Content-type:text/html\r\n\r\n")
            print('<html>')
            print('<head><title>loginwrong</title></head>')
            print("<body background='../images.jpeg'>")
            print("<form action='/ludotemplate.html'>")
            print('<br/><br/><br/><br/><br/><br/><br/><br/><br/><center><input type="submit" style="width:22em; height:8em; font-size:2em" value="Password entered is wrong, click to login again"/></center>')
            print('</form>')
            print('</body></html>')
            flag=1
            break
if flag==0:
    print('<html>')
    print('<head><title>loginwrong</title></head>')
    print("<body background='../images.jpeg'>")
    print("<form action='/ludotemplate.html'>")
    print('<br/><br/><br/><br/><br/><br/><br/><br/><br/><center><input type="submit" style="width:22em; height:8em; font-size:2em" value="Username entered is wrong, click to login again"/></center>')
    print('</form>')
    print('</body></html>')

        