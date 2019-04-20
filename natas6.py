import requests
import re
username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org" % username

#custom_cookies = {"loggedin":"1"}

session = requests.Session()
response = session.post(url, data={"secret": "FOEIUWGHFEEUHOFUOIU","submit":"submit"}, auth = (username, password))

content = response.text

#print(content)
print(re.findall('natas7 is (.*)', content)[0])
