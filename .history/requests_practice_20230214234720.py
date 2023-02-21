import requests
import os

url = 'https://weatherapi-com.p.rapidapi.com/future.json'

key="X-RapidAPI-Key"
host="X-RapidAPI-Host"

headers = {
	"X-RapidAPI-Key": os.getenv(key)#"9361cc9094msh35fd29499505acep1c5190jsn4523644ac586",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}