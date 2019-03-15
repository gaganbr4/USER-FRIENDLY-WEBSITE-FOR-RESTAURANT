#!/usr/bin/env python3
import back
import cgi
import json

print("Content-type:text/html\r\n\r\n")

with open("../html/after/profile.json", "r") as read_file:
    data = json.load(read_file)
    name=data["User"][0]["Username"]

rows=back.search(name)

a=rows[len(rows)-1]
b=a[2].split('_')

print('<html>')
print('<head><title>Success</title></head>')
print('<body bgcolor= maroon; color: yellow>')
print('<center><h2>Payment successful! Your order is placed</h2><br>Order ID : #'+str(a[0])+'</center>')
for i in b:
    print('<br>'+i)
print('<br><br><br>Bill Amount : Rs.'+str(a[3]))
print('</body></html>')
