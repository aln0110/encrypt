#from conn import dataBase
#from user import User
#from encrypt import Encrypt

import socket
#import json
import requests
#import random



def main():
    myIP= requests.get('https://api.ipify.org').text
    url= f'http://ip-api.com/json/{myIP}'
    response = requests.get(url)
    location = response.json()
    lon = location['lon']
    lat = location['lat']
    
    urlW = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=7f874c11dbddd349b40fcfd82765d0f3&units=metric'
    weather= requests.get(urlW)
    
    #print(f'Weather thing:  {weather.json()}')
   
    urlR= "https://api.random.org/json-rpc/4/invoke" 
    
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "7406367f-407d-44a6-91b1-a9daf911be6b",
            "n": 1,
            "min": -115251252,
            "max": 925245125,
            "replacement": True
        },
        "id": 42
    }
    #rand= requests.post(urlR, json=payload, headers=headers)
   # print(f'Random number: {rand.json()}')
 
    for i in range(0, 5):
   #     rand= requests.post(urlR, json=payload, headers=headers)
   #     print(f'Random number: {rand.json()}')
        pass
 
    pass


if __name__ == '__main__':
    main()
    