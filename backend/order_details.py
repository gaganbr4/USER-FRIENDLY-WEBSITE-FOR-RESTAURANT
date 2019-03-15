#!/usr/bin/env python3
import back
import cgi
import json

print("Content-type:text/html\r\n\r\n")

with open("../html/after/profile.json", "r") as read_file:
    data = json.load(read_file)
    name=data["User"][0]["Username"]

rows=back.search(name)

data={}
data['Order']=[]
for a in rows:
	b=str(a[2])
	b=b.replace("_",",")
	temp="{\"ID\" "+": \""+str(a[0])+"\","+" \"Details\""+": \""+b+"\","+" \"Sum\""+": \""+str(a[3])+"\"}"
	temp = json.loads(temp)
	data['Order'].append(temp)
with open('../html/after/orders.json', 'w') as outfile:
    json.dump(data, outfile)

redirectURL = "http://localhost/after/history.html"
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >')
print('</head>')
print('</html>')
