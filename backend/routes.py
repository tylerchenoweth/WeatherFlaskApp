from app import app

import random, requests, json, time, pandas as pd, numpy as np 
from datetime import datetime
from dotenv import load_dotenv
import os, json
from flask import jsonify
from flask_cors import cross_origin



def kelvin_to_fahrenheit(kelvin):
    kelvin = float(kelvin)

    if kelvin < 0:
        raise ValueError("Temperature in Kelvin cannot be below absolute zero (0 K).")

    fahrenheit = round( ((kelvin - 273.15) * 9/5 + 32), 0)
    return fahrenheit


def epoch_to_day_of_week(epoch_time):
    return time.strftime('%A', time.gmtime(epoch_time))


def epoch_to_datetime(epoch_time):
    return datetime.fromtimestamp(epoch_time)

def epoch_to_standard_time(epoch_time):
    return datetime.fromtimestamp(epoch_time).strftime("%I:%M:%S %p")

def getLatLongByCity(cityName, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={cityName}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Check if the city is in a state
    try:
        state = data[0]['state']
    except:
        state = None

    geo = {
        "city": data[0]['name'],
        "state": state,
        "country": data[0]['country'],
        "lat": data[0]['lat'],
        "long": data[0]['lon'],
    }

    return geo


def getWeatherDataWLatLong(lat, long, api_key):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()

    return data



@app.route('/')
@cross_origin(origin='http://localhost:3000')
def index():
    
    # Hard coded coordinates for Tampa
    # lat = 27.9574621
    # long = -82.4597585

    # https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API key}

    # This url is used to get lat and long coords by city name
    # http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

    # url = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(lat)+"&lon="+str(long)+"&appid="+API_Key


    #########################################################################################################################


    # load_dotenv()
    # api_key = os.getenv('API_KEY')
    
    api_key = ""

    # The weather icon will be put between these two elements
    # to get the full URL
    icon_url = [
        "https://openweathermap.org/img/wn/",
        "@2x.png"
    ]


    # Declare blank variables to load later

    # Holds all the data retrieved from the API
    data = {}
    # Holds geographic data of the city
    geo = {}
    # Holds the data for the future weather
    forecast = {}
    # Holds data{}, forecast{}, now{} and gets returned
    context = {}

    # Determine if were working with current or offline data
    # If there is no API Key then just use offline data
    if(api_key == ""):
        # Load data from json file when working without api requests
        with open('./offlineData.json', 'r') as file:
            fileData = json.load(file)

            geo = fileData['CityDetails']
            data = fileData['WeatherData']
    else:
        # Get basic info about the city
        geo = getLatLongByCity("tampa", api_key)

        # Get weather data
        data = getWeatherDataWLatLong(geo['lat'], geo['long'], api_key)


    # Get the forecast from the json
    for num, i in enumerate(data['daily']):
        forecast[num] = {
            "day": epoch_to_day_of_week(i['dt']),
            "datetime": epoch_to_datetime(i['dt']),
            "summary": i['summary'],
            "temp": round(i['temp']['day'], 0),
            "feels_like": round(i['feels_like']['day'], 0),
            "max_temp": round(i['temp']['max'], 0),
            "min_temp": round(i['temp']['min'], 0),
            "humidity": i['humidity'],
            "dew_point": i['dew_point'],
            "sunrise": epoch_to_standard_time(i['sunrise']),
            "sunset": epoch_to_standard_time(i['sunset']),
            "uvi": i["uvi"],
            "wind_direction": i['wind_deg'],
            "wind_speed": i['wind_speed'],
            "wind_gust": i['wind_gust'],
            "weather": {
                "description": i['weather'][0]['description'],
                "icon": icon_url[0] + i['weather'][0]['icon'] + icon_url[1]
            },
            "summary": i['summary']
        }  

    # Check if there are weather alerts
    try:
        alerts = data['alerts']
    except:
        alerts = None

    # Get the current weather
    now = {
        "alerts": alerts,
        "lat": data['lat'],
        "long": data['lon'],
        "temp": round(data['current']['temp'], 0),
        "feels_like": round(data['current']['feels_like'], 0),
        "humidity": data['current']['humidity'],
        "uvi": data['current']["uvi"],
        "wind_direction": data['current']['wind_deg'],
        "wind_speed": data['current']['wind_speed'],
        "timestamp": epoch_to_datetime(data['current']['dt']),
        "weather": {
            "description": data['current']['weather'][0]['description'],
            "icon": icon_url[0] + data['current']['weather'][0]['icon'] + icon_url[1]
        }
    }

    # Load context
    context['now'] = now
    context['forecast'] = forecast
    context['geo'] = geo
    
    
    # return data
    return jsonify(context)
    # return forecast
    