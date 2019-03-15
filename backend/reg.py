#!/usr/bin/env python3
import back
import cgi
import json

print("Content-type:text/html\r\n\r\n")
form=cgi.FieldStorage()
uname=form.getvalue('username')
pswd1=form.getvalue('password')
pswd2 = form.getvalue('pswd')
mobile=form.getvalue('mobile')
address=form.getvalue('address')

if pswd1==pswd2:
    back.create()
    back.insert(uname,pswd1,mobile,address)
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

else:
    redirectURL = "http://localhost/after/reg_fail.html"
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >')
    print('</head>')
    print('</html>')
