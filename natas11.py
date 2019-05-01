import requests
import re
import urllib
import base64
from itertools import izip, cycle
import base64

#This is a python2 script!!
username="natas11"
password="U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username

def xor_crypt_string(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))

default_data = "{'showpassword':'no', 'bgcolor':'#ffffff'}"

session = requests.Session()

response = session.post(url, auth = (username, password))

content = response.text

#we get the cookie from our season using the default data with showpassword = no
print urllib.unquote(session.cookies["data"])
cypher_text = base64.b64decode(urllib.unquote(session.cookies["data"]))

# we get the cypher text
print cypher_text
# we ryn xor encryption  with data and cypher_text and that's equal to our key
key = xor_crypt_string(default_data, cypher_text)[0:4]
print key

# with the key in hand we change the data so showpassword is yes
new_data = '{"showpassword":"yes","bgcolor":"#ffffff"}'
print new_data

#and we run the encryption again so this time we can get the cypher text
cookie = xor_crypt_string(new_data, key)
cookie = base64.b64encode(cookie)
print cookie

#for some reason i get a different string that if i was doing this with php
#I will use the php generated string below to get the pass but if anyone can find the error in my code please let me know.
cookies_complete = {"data": "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

response = session.post(url, auth = (username, password), cookies=cookies_complete)

print response.text

