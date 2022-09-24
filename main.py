from urllib import request
import requests
import re
import os 
from datetime import datetime
api_user = os.environ['current_temp']
print ("****************WELCOME TO WEATHER DETECTOR****************",)
print("\n")
print ("*************PRESS 1 TO CONTINUE AND 0 TO EXIT*************")
h= int(input())
while(h==1):
    place = input("Enter the name of the place whose weather is to be detected : ")
    if((place.isdigit()) and (bool(re.match('^[a-zA-Z0-9]*$', place)) != True)):
        print("YOU ENTERED A INTEGER IN NAME OF THE PLACE")
    else:
        print(f"If you want current temperature of {place} type 'c' and if you want weather foreacast of next few hours of {place} press 'f' ")
        choice = input()
        date_and_time =  datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        if(choice =="c"):
                link = "https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid="+api_user
                call_api = requests.get(link)
                info = call_api.json()
                if info['cod']=='404':
                    print("Invalid Location")
                else:
                    temp = (info['main']['temp'])-273.15
                    weather = info['weather'][0]['description']
                    humidity = info['main']['humidity']
                    # wind_speed = info['main'][1]['speed']
                    date_and_time =  datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
                print(f"  THE CURRENT DATE AND TIME IS : {date_and_time} ")
                print(f"  THE CURRENT TEMPERATURE OF {place} IS {temp}")
                print(f"  THE CURRENT WEATHER OF {place} IS {weather}")
                print(f"  THE CURRENT HUMIDITY OF {place} IS {humidity}")

        elif(choice=="f"):
            state_code="dl"
            country_code= "91"
            link_lat_long= "http://api.openweathermap.org/geo/1.0/direct?q="+place+"&limit=5&appid="+api_user
            call_api2 = requests.get(link_lat_long)
            info2 = call_api2.json()
            latitude = info2[1]['lat']
            longitude  =info2[1]['lon']
            str_lat =str(latitude)
            str_lon =str(longitude)

            link_forecast="http://api.openweathermap.org/data/2.5/forecast?lat="+str_lat+"&lon="+str_lon+"&appid="+api_user
            call_api3= requests.get(link_forecast)
            info3 = call_api3.json()
            # after three hour desciption
            temp_1=((info3['list'][0]['main']['temp'])-273.15)
            descrip = ((info3['list'][0]['weather'][0]['description']))
            #after three hours description(1)
            temp_2 = ((info3['list'][1]['main']['temp'])-273.15)
            descrip2= ((info3['list'][1]['weather'][0]['description']))
            #after three hours description(2)
            temp_3= ((info3['list'][2]['main']['temp'])-273.15)
            descrip3= ((info3['list'][2]['weather'][0]['description']))
            print(f"  THE CURRENT DATE AND TIME IS : {date_and_time} ")
            print(f"  The Temperature of {place} after 3 hour is :{temp_1} and the description is {descrip}")
            print(f"  The Temperature of {place} after 3 hour is :{temp_2} and the description is {descrip2}")
            print(f"  The Temperature of {place} after 3 hour is :{temp_3} and the description is {descrip3}")
    print ("*************PRESS 1 TO CONTINUE AND 0 TO EXIT*************")
    h=int(input())
