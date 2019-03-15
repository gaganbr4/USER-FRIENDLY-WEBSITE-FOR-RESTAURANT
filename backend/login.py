#!/usr/bin/env python3
import cgi
import back
import json

print("Content-type:text/html\r\n\r\n")
form=cgi.FieldStorage()
uname=form.getvalue('username')
password=form.getvalue('password')
flag=0
cur=back.validate()


for row in cur:
    if row[0]==uname:
        if row[1]==password:
            rows=back.view(uname)
            data = {}
            data['User'] = []
            for a in rows:
                temp="{\"Username\" "+": \""+str(a[0])+"\","+" \"Mobile\""+": \""+str(a[2])+"\","+" \"Address\""+": \""+str(a[3])+"\"}"
                temp = json.loads(temp)
                data['User'].append(temp)
            with open('../html/after/profile.json', 'w') as outfile:
                json.dump(data, outfile)
            redirectURL = "http://localhost/after/index.html"
            print("Content-type:text/html\r\n\r\n")
            print('<html>')
            print('<head>')
            print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >')
            print('</head>')
            print('</html>')
            flag=1
            break
        else:
            #messagebox.showinfo('Re','Passwords do not match. Re-type passwords')
            #print("Content-type:text/html\r\n\r\n")
            redirectURL = "http://localhost/after/login_fail.html"
            print("Content-type:text/html\r\n\r\n")
            print('<html>')
            print('<head>')
            print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >')
            print('</head>')
            print('</html>')
            flag=1
            break
if flag==0:
    redirectURL = "http://localhost/after/login_fail.html"
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >')
    print('</head>')
    print('</html>')
