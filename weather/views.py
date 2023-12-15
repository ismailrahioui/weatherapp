import datetime as dt
from django.shortcuts import render
import json 
import urllib.request

import requests

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        url=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=7f5dfa11493b278c5761b6f85f45432a').read()
        json_data=json.loads(url)
      
        
         
        data={
            "county_code":str(json_data['sys']['country']),
            "temp":int(json_data['main']['temp']-273.15 ),
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
            "sunrise":dt.datetime.utcfromtimestamp((json_data['sys']['sunrise'])+json_data['timezone']),
            "wind":round(json_data['wind']['speed'],1),
            "description":str(json_data['weather'][0]['description']),
            "icon":str(json_data['weather'][0]['icon']),
            "time": dt.date.fromtimestamp(json_data['dt']),
            "visibility": float(json_data['visibility']/1000),
        }
        print(json_data)
    else:
        city =''
        data = {}
    return render(request,'index.html',{'city':city,'data':data})


