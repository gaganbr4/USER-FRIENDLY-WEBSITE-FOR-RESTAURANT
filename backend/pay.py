#!/usr/bin/env python3
import back
import cgi
import json

print("Content-type:text/html\r\n\r\n")
form=cgi.FieldStorage()
details=form.getvalue('details')
sum=form.getvalue('sum')
card=form.getvalue('cardNumber')
exp=form.getvalue('EXPIRATION')
cvv=form.getvalue('cvv')

if(len(card)==16):
    if(len(cvv)==3):
        with open("../html/after/profile.json", "r") as read_file:
            data = json.load(read_file)
            name=data["User"][0]["Username"]

        back.create2()
        back.insert2(name,details,sum)

        redirectURL = "http://localhost/cgi-bin/success.py"
        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >')
        print('</head>')
        print('</html>')
else:
        redirectURL = "http://localhost/after/payment_fail.html"
        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >')
        print('</head>')
        print('</html>')
