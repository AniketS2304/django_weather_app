from django.shortcuts import render
import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
def home(request):
    api = os.getenv('API_key')
    city_name = request.POST.get("city", "Pune")
      
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}"
    PARAMS = {"units": "metric"}

    response= requests.get(url, params=PARAMS)
    data = response.json()

    if response.status_code == 200 and 'weather' in data:
        
        desc = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()
    else:
        desc = "City not found or API error"
        icon = "01d"
        temp = "N/A"
        
    payload = {
        'desc': desc,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city_name
    }

    return render(request, 'index.html', payload)
