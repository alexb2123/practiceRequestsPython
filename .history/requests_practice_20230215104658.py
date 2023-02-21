import requests
import os

url = 'https://national-weather-service.p.rapidapi.com/zones/%7Btype%7D/%7BzoneId%7D/forecas'

key="X-RapidAPI-Key"
host="X-RapidAPI-Host"

#querystring = {"q":"London","dt":"2022-12-25"}

#print("this is the key",os.getenv(key, default=None))


headers = {
	"X-RapidAPI-Key": "06bc7e589fmsh3afac84d321746cp14623djsna2c6710074e4",#os.getenv(key),#"9361cc9094msh35fd29499505acep1c5190jsn4523644ac586",
	"X-RapidAPI-Host": os.getenv(host)#"weatherapi-com.p.rapidapi.com"
}

#response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)