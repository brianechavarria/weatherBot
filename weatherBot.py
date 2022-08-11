import requests
import datetime
from twilio.rest import Client

with open('SensitiveInfo.txt') as f:
    lines = f.read().splitlines()

weatherapi = str(lines[0])
account_sid = str(lines[1])
auth_token = str(lines[2])
FROM = str(lines[3])
TO = str(lines[4])



city = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=New York&limit=5&appid=' + weatherapi)
city = city.json()
name = city[0]['name']

lat, lon = city[0]['lat'] , city[0]['lon']

baseURL = 'https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&units=imperial&appid=' + weatherapi

weather = (requests.get(baseURL)).json()


conditions = weather['main']

temp = str(conditions['temp'])
realFeel = str(conditions['feels_like'])
humidity = str(conditions['humidity'])


weather = weather['weather']
weather = str(weather[0]['description'])

now = (datetime.datetime.now()).date()


text=str(now) + " - Weather in " + name + ": " + weather + ", temp: " + temp + ", real feel: " + realFeel + ", humidity: " + humidity + "%" 


client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body=text,
         from_=FROM,
         to=TO
     )
    
    
print("Message Sent Successfully")