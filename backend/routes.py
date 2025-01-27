from app import app

import random, requests, json, time, pandas as pd, numpy as np 
from datetime import datetime
from dotenv import load_dotenv
import os
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


def getLatLongByCity(cityName, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={cityName}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Check if the city is in a state
    try:
        state = data[0]['state']
        print("a;lskdjf;laskjdf")
    except:
        print("NONEONEONEONEONOE")
        state = None

    geo = {
        "city": data[0]['name'],
        "state": state,
        "country": data[0]['country'],
        "lat": data[0]['lat'],
        "long": data[0]['lon'],
    }

    return geo


def getDataWLatLong(lat, long, api_key):

    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()

    return data



@app.route('/')
@cross_origin(origin='http://localhost:3000')
def index():
    
    
    lat = 27.9574621
    long = -82.4597585

    # https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API key}

    # This url is used to get lat and long coords by city name
    # http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}


    # url = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(lat)+"&lon="+str(long)+"&appid="+API_Key

    

    # Offline data
    geo = {"city":"Tampa","country":"US","lat":27.9477595,"long":-82.458444,"state":"Florida"}

    data = {"current":{"clouds":75,"dew_point":43.02,"dt":1737853874,"feels_like":50,"humidity":72,"pressure":1029,"sunrise":1737807589,"sunset":1737846261,"temp":51.75,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":340,"wind_speed":5.75},"daily":[{"clouds":22,"dew_point":33.3,"dt":1737824400,"feels_like":{"day":52.97,"eve":52.59,"morn":33.67,"night":50.27},"humidity":43,"moon_phase":0.87,"moonrise":1737795960,"moonset":1737832620,"pop":0,"pressure":1031,"summary":"There will be clear sky until morning, then partly cloudy","sunrise":1737807589,"sunset":1737846261,"temp":{"day":55.69,"eve":54.52,"max":60.82,"min":39.69,"morn":40.26,"night":52.07},"uvi":4.94,"weather":[{"description":"few clouds","icon":"02d","id":801,"main":"Clouds"}],"wind_deg":11,"wind_gust":23.78,"wind_speed":12.57},{"clouds":78,"dew_point":46.99,"dt":1737910800,"feels_like":{"day":61.75,"eve":62.29,"morn":45.54,"night":55.56},"humidity":56,"moon_phase":0.9,"moonrise":1737885900,"moonset":1737922380,"pop":0,"pressure":1029,"summary":"You can expect partly cloudy in the morning, with clearing in the afternoon","sunrise":1737893967,"sunset":1737932711,"temp":{"day":63.1,"eve":63.64,"max":66.72,"min":48.88,"morn":49.1,"night":56.68},"uvi":4.75,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":44,"wind_gust":16.98,"wind_speed":9.86},{"clouds":89,"dew_point":50,"dt":1737997200,"feels_like":{"day":63.52,"eve":62.2,"morn":52.41,"night":57.24},"humidity":60,"moon_phase":0.94,"moonrise":1737975600,"moonset":1738012440,"pop":0,"pressure":1025,"summary":"Expect a day of partly cloudy with clear spells","sunrise":1737980343,"sunset":1738019160,"temp":{"day":64.54,"eve":63.43,"max":65.93,"min":53.31,"morn":53.42,"night":58.37},"uvi":4.5,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":96,"wind_gust":15.41,"wind_speed":7.11},{"clouds":9,"dew_point":53.01,"dt":1738083600,"feels_like":{"day":65.25,"eve":63.91,"morn":54.68,"night":60.57},"humidity":64,"moon_phase":0.97,"moonrise":1738065060,"moonset":1738102800,"pop":0,"pressure":1021,"summary":"Expect a day of partly cloudy with clear spells","sunrise":1738066718,"sunset":1738105610,"temp":{"day":65.95,"eve":64.44,"max":67.55,"min":55.44,"morn":55.53,"night":60.84},"uvi":5.07,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":294,"wind_gust":10.78,"wind_speed":9.15},{"clouds":73,"dew_point":55.31,"dt":1738170000,"feels_like":{"day":66.69,"eve":63.36,"morn":56.62,"night":61.07},"humidity":67,"moon_phase":0,"moonrise":1738154160,"moonset":1738193220,"pop":0,"pressure":1021,"summary":"There will be partly cloudy today","sunrise":1738153092,"sunset":1738192059,"temp":{"day":67.12,"eve":63.81,"max":67.26,"min":56.82,"morn":56.82,"night":61.38},"uvi":5.16,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":276,"wind_gust":7.67,"wind_speed":5.95},{"clouds":30,"dew_point":53.35,"dt":1738256400,"feels_like":{"day":70.83,"eve":68.02,"morn":57.49,"night":64.4},"humidity":53,"moon_phase":0.04,"moonrise":1738242960,"moonset":1738283640,"pop":0,"pressure":1022,"summary":"Expect a day of partly cloudy with clear spells","sunrise":1738239464,"sunset":1738278508,"temp":{"day":71.49,"eve":68.63,"max":73.53,"min":57.9,"morn":57.9,"night":64.87},"uvi":6,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":89,"wind_gust":18.95,"wind_speed":10.49},{"clouds":76,"dew_point":54.88,"dt":1738342800,"feels_like":{"day":71.69,"eve":67.64,"morn":58.68,"night":66.06},"humidity":54,"moon_phase":0.08,"moonrise":1738331520,"moonset":1738373940,"pop":0,"pressure":1025,"summary":"There will be partly cloudy today","sunrise":1738325834,"sunset":1738364957,"temp":{"day":72.23,"eve":68.2,"max":73.6,"min":58.82,"morn":58.82,"night":66.34},"uvi":6,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":79,"wind_gust":28.1,"wind_speed":16.13},{"clouds":27,"dew_point":53.92,"dt":1738429200,"feels_like":{"day":70.61,"eve":67.37,"morn":60.82,"night":62.58},"humidity":55,"moon_phase":0.12,"moonrise":1738419960,"moonset":1738464240,"pop":0,"pressure":1026,"summary":"There will be partly cloudy today","sunrise":1738412204,"sunset":1738451405,"temp":{"day":71.2,"eve":67.87,"max":71.2,"min":61.41,"morn":61.41,"night":63.01},"uvi":6,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":100,"wind_gust":31.09,"wind_speed":19.24}],"hourly":[{"clouds":75,"dew_point":43.02,"dt":1737853200,"feels_like":50,"humidity":72,"pop":0,"pressure":1029,"temp":51.75,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":52,"wind_gust":15.35,"wind_speed":8.19},{"clouds":80,"dew_point":42.73,"dt":1737856800,"feels_like":50.41,"humidity":70,"pop":0,"pressure":1029,"temp":52.2,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":56,"wind_gust":16.82,"wind_speed":8.34},{"clouds":85,"dew_point":42.8,"dt":1737860400,"feels_like":50.49,"humidity":70,"pop":0,"pressure":1029,"temp":52.27,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":60,"wind_gust":17.16,"wind_speed":7.99},{"clouds":89,"dew_point":42.6,"dt":1737864000,"feels_like":50.27,"humidity":70,"pop":0,"pressure":1029,"temp":52.07,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":61,"wind_gust":18.28,"wind_speed":9.08},{"clouds":94,"dew_point":42.55,"dt":1737867600,"feels_like":49.82,"humidity":71,"pop":0,"pressure":1029,"temp":51.62,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":63,"wind_gust":16.4,"wind_speed":7.76},{"clouds":99,"dew_point":42.62,"dt":1737871200,"feels_like":49.24,"humidity":72,"pop":0,"pressure":1029,"temp":51.06,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":60,"wind_gust":14.97,"wind_speed":7.58},{"clouds":100,"dew_point":42.4,"dt":1737874800,"feels_like":48.81,"humidity":74,"pop":0,"pressure":1029,"temp":50.58,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":55,"wind_gust":13.42,"wind_speed":7.05},{"clouds":100,"dew_point":42.39,"dt":1737878400,"feels_like":48.42,"humidity":75,"pop":0,"pressure":1028,"temp":50.18,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":52,"wind_gust":13.85,"wind_speed":7.83},{"clouds":99,"dew_point":42.42,"dt":1737882000,"feels_like":46.74,"humidity":76,"pop":0,"pressure":1028,"temp":49.86,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":50,"wind_gust":13.49,"wind_speed":7.63},{"clouds":92,"dew_point":42.58,"dt":1737885600,"feels_like":46.15,"humidity":77,"pop":0,"pressure":1028,"temp":49.46,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":40,"wind_gust":12.97,"wind_speed":7.92},{"clouds":94,"dew_point":42.71,"dt":1737889200,"feels_like":45.54,"humidity":79,"pop":0,"pressure":1029,"temp":49.1,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":39,"wind_gust":13.76,"wind_speed":8.34},{"clouds":96,"dew_point":42.78,"dt":1737892800,"feels_like":45.12,"humidity":79,"pop":0,"pressure":1030,"temp":48.88,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":38,"wind_gust":15.64,"wind_speed":8.7},{"clouds":100,"dew_point":42.93,"dt":1737896400,"feels_like":45.61,"humidity":79,"pop":0,"pressure":1030,"temp":49.24,"uvi":0.27,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":39,"wind_gust":15.88,"wind_speed":8.61},{"clouds":83,"dew_point":43.68,"dt":1737900000,"feels_like":50.61,"humidity":72,"pop":0,"pressure":1030,"temp":52.3,"uvi":1.09,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":44,"wind_gust":15.52,"wind_speed":9.86},{"clouds":88,"dew_point":44.83,"dt":1737903600,"feels_like":54.63,"humidity":66,"pop":0,"pressure":1030,"temp":56.21,"uvi":2.43,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":58,"wind_gust":13.76,"wind_speed":9.73},{"clouds":91,"dew_point":46.17,"dt":1737907200,"feels_like":58.59,"humidity":60,"pop":0,"pressure":1029,"temp":60.06,"uvi":3.89,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":72,"wind_gust":12.08,"wind_speed":8.55},{"clouds":78,"dew_point":46.99,"dt":1737910800,"feels_like":61.75,"humidity":56,"pop":0,"pressure":1029,"temp":63.1,"uvi":4.75,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":83,"wind_gust":9.95,"wind_speed":7.2},{"clouds":65,"dew_point":46.96,"dt":1737914400,"feels_like":63.54,"humidity":52,"pop":0,"pressure":1027,"temp":64.9,"uvi":4.74,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":82,"wind_gust":7.63,"wind_speed":5.82},{"clouds":1,"dew_point":46.85,"dt":1737918000,"feels_like":64.62,"humidity":50,"pop":0,"pressure":1027,"temp":65.97,"uvi":3.81,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":65,"wind_gust":6.46,"wind_speed":4.9},{"clouds":0,"dew_point":46.8,"dt":1737921600,"feels_like":65.3,"humidity":49,"pop":0,"pressure":1026,"temp":66.63,"uvi":2.37,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":61,"wind_gust":5.41,"wind_speed":4},{"clouds":0,"dew_point":46.78,"dt":1737925200,"feels_like":65.39,"humidity":49,"pop":0,"pressure":1026,"temp":66.72,"uvi":1.04,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":67,"wind_gust":5.95,"wind_speed":4.43},{"clouds":0,"dew_point":47.08,"dt":1737928800,"feels_like":64.98,"humidity":50,"pop":0,"pressure":1026,"temp":66.29,"uvi":0.26,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":67,"wind_gust":6.31,"wind_speed":4.76},{"clouds":0,"dew_point":47.39,"dt":1737932400,"feels_like":62.29,"humidity":55,"pop":0,"pressure":1026,"temp":63.64,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":57,"wind_gust":4.7,"wind_speed":3.78},{"clouds":0,"dew_point":47.35,"dt":1737936000,"feels_like":60.39,"humidity":59,"pop":0,"pressure":1026,"temp":61.74,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":29,"wind_gust":4.61,"wind_speed":3.94},{"clouds":4,"dew_point":47.08,"dt":1737939600,"feels_like":59.14,"humidity":61,"pop":0,"pressure":1026,"temp":60.53,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":42,"wind_gust":8.01,"wind_speed":5.46},{"clouds":3,"dew_point":46.69,"dt":1737943200,"feels_like":58.1,"humidity":63,"pop":0,"pressure":1026,"temp":59.49,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":76,"wind_gust":12.68,"wind_speed":7.2},{"clouds":3,"dew_point":47.48,"dt":1737946800,"feels_like":56.53,"humidity":68,"pop":0,"pressure":1026,"temp":57.85,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":85,"wind_gust":16.98,"wind_speed":8.23},{"clouds":10,"dew_point":48.81,"dt":1737950400,"feels_like":55.56,"humidity":75,"pop":0,"pressure":1026,"temp":56.68,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":90,"wind_gust":15.97,"wind_speed":7.36},{"clouds":14,"dew_point":48.7,"dt":1737954000,"feels_like":54.77,"humidity":77,"pop":0,"pressure":1025,"temp":55.87,"uvi":0,"visibility":10000,"weather":[{"description":"few clouds","icon":"02n","id":801,"main":"Clouds"}],"wind_deg":96,"wind_gust":15.41,"wind_speed":7.11},{"clouds":22,"dew_point":48.49,"dt":1737957600,"feels_like":54.05,"humidity":78,"pop":0,"pressure":1025,"temp":55.17,"uvi":0,"visibility":10000,"weather":[{"description":"few clouds","icon":"02n","id":801,"main":"Clouds"}],"wind_deg":94,"wind_gust":12.48,"wind_speed":6.33},{"clouds":99,"dew_point":48.4,"dt":1737961200,"feels_like":53.64,"humidity":79,"pop":0,"pressure":1025,"temp":54.75,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":90,"wind_gust":9.22,"wind_speed":5.48},{"clouds":98,"dew_point":48.42,"dt":1737964800,"feels_like":53.2,"humidity":80,"pop":0,"pressure":1024,"temp":54.32,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":91,"wind_gust":8.01,"wind_speed":5.28},{"clouds":99,"dew_point":48.49,"dt":1737968400,"feels_like":53.04,"humidity":81,"pop":0,"pressure":1024,"temp":54.12,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":89,"wind_gust":6.29,"wind_speed":5.3},{"clouds":79,"dew_point":48.61,"dt":1737972000,"feels_like":52.65,"humidity":83,"pop":0,"pressure":1024,"temp":53.67,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":74,"wind_gust":4.5,"wind_speed":4.63},{"clouds":64,"dew_point":48.78,"dt":1737975600,"feels_like":52.41,"humidity":84,"pop":0,"pressure":1024,"temp":53.42,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":87,"wind_gust":4.99,"wind_speed":5.08},{"clouds":70,"dew_point":48.88,"dt":1737979200,"feels_like":52.34,"humidity":85,"pop":0,"pressure":1024,"temp":53.31,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":80,"wind_gust":5.3,"wind_speed":5.35},{"clouds":100,"dew_point":49.12,"dt":1737982800,"feels_like":52.99,"humidity":84,"pop":0,"pressure":1024,"temp":53.94,"uvi":0.26,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":91,"wind_gust":6.04,"wind_speed":5.21},{"clouds":100,"dew_point":49.55,"dt":1737986400,"feels_like":55.6,"humidity":77,"pop":0,"pressure":1025,"temp":56.62,"uvi":1.08,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":89,"wind_gust":6.38,"wind_speed":4.9},{"clouds":100,"dew_point":49.95,"dt":1737990000,"feels_like":58.8,"humidity":70,"pop":0,"pressure":1025,"temp":59.83,"uvi":2.31,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":102,"wind_gust":4.97,"wind_speed":4.16},{"clouds":86,"dew_point":50.22,"dt":1737993600,"feels_like":61.65,"humidity":64,"pop":0,"pressure":1025,"temp":62.67,"uvi":3.85,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":121,"wind_gust":5.08,"wind_speed":4.05},{"clouds":89,"dew_point":50,"dt":1737997200,"feels_like":63.52,"humidity":60,"pop":0,"pressure":1025,"temp":64.54,"uvi":4.45,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":148,"wind_gust":1.74,"wind_speed":0.63},{"clouds":91,"dew_point":49.24,"dt":1738000800,"feels_like":64.4,"humidity":56,"pop":0,"pressure":1023,"temp":65.52,"uvi":4.5,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":237,"wind_gust":2.24,"wind_speed":2.73},{"clouds":100,"dew_point":48.45,"dt":1738004400,"feels_like":64.69,"humidity":55,"pop":0,"pressure":1022,"temp":65.82,"uvi":3.59,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":264,"wind_gust":3.31,"wind_speed":4.65},{"clouds":100,"dew_point":47.66,"dt":1738008000,"feels_like":64.71,"humidity":53,"pop":0,"pressure":1021,"temp":65.93,"uvi":2.37,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":262,"wind_gust":3.6,"wind_speed":4.72},{"clouds":100,"dew_point":47.5,"dt":1738011600,"feels_like":64.69,"humidity":53,"pop":0,"pressure":1021,"temp":65.91,"uvi":0.99,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":276,"wind_gust":4.83,"wind_speed":6.02},{"clouds":100,"dew_point":47.7,"dt":1738015200,"feels_like":64.04,"humidity":54,"pop":0,"pressure":1021,"temp":65.28,"uvi":0.24,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":277,"wind_gust":3.98,"wind_speed":5.53},{"clouds":100,"dew_point":48.22,"dt":1738018800,"feels_like":62.2,"humidity":58,"pop":0,"pressure":1021,"temp":63.43,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":290,"wind_gust":7.25,"wind_speed":6.11},{"clouds":97,"dew_point":49.05,"dt":1738022400,"feels_like":60.57,"humidity":63,"pop":0,"pressure":1021,"temp":61.74,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":317,"wind_gust":8.41,"wind_speed":6.58}],"lat":27.9478,"lon":-82.4584,"minutely":[{"dt":1737853920,"precipitation":0},{"dt":1737853980,"precipitation":0},{"dt":1737854040,"precipitation":0},{"dt":1737854100,"precipitation":0},{"dt":1737854160,"precipitation":0},{"dt":1737854220,"precipitation":0},{"dt":1737854280,"precipitation":0},{"dt":1737854340,"precipitation":0},{"dt":1737854400,"precipitation":0},{"dt":1737854460,"precipitation":0},{"dt":1737854520,"precipitation":0},{"dt":1737854580,"precipitation":0},{"dt":1737854640,"precipitation":0},{"dt":1737854700,"precipitation":0},{"dt":1737854760,"precipitation":0},{"dt":1737854820,"precipitation":0},{"dt":1737854880,"precipitation":0},{"dt":1737854940,"precipitation":0},{"dt":1737855000,"precipitation":0},{"dt":1737855060,"precipitation":0},{"dt":1737855120,"precipitation":0},{"dt":1737855180,"precipitation":0},{"dt":1737855240,"precipitation":0},{"dt":1737855300,"precipitation":0},{"dt":1737855360,"precipitation":0},{"dt":1737855420,"precipitation":0},{"dt":1737855480,"precipitation":0},{"dt":1737855540,"precipitation":0},{"dt":1737855600,"precipitation":0},{"dt":1737855660,"precipitation":0},{"dt":1737855720,"precipitation":0},{"dt":1737855780,"precipitation":0},{"dt":1737855840,"precipitation":0},{"dt":1737855900,"precipitation":0},{"dt":1737855960,"precipitation":0},{"dt":1737856020,"precipitation":0},{"dt":1737856080,"precipitation":0},{"dt":1737856140,"precipitation":0},{"dt":1737856200,"precipitation":0},{"dt":1737856260,"precipitation":0},{"dt":1737856320,"precipitation":0},{"dt":1737856380,"precipitation":0},{"dt":1737856440,"precipitation":0},{"dt":1737856500,"precipitation":0},{"dt":1737856560,"precipitation":0},{"dt":1737856620,"precipitation":0},{"dt":1737856680,"precipitation":0},{"dt":1737856740,"precipitation":0},{"dt":1737856800,"precipitation":0},{"dt":1737856860,"precipitation":0},{"dt":1737856920,"precipitation":0},{"dt":1737856980,"precipitation":0},{"dt":1737857040,"precipitation":0},{"dt":1737857100,"precipitation":0},{"dt":1737857160,"precipitation":0},{"dt":1737857220,"precipitation":0},{"dt":1737857280,"precipitation":0},{"dt":1737857340,"precipitation":0},{"dt":1737857400,"precipitation":0},{"dt":1737857460,"precipitation":0}],"timezone":"America/New_York","timezone_offset":-18000}






    load_dotenv()
    api_key = os.getenv('API_KEY')
    api_key = ""
    icon_url = [
        "https://openweathermap.org/img/wn/",
        "@2x.png"
    ]

    # Comment below for offline mode
    # Get basic info about the city
    # geo = getLatLongByCity("tampa", api_key)

    # Get weather data
    # data = getDataWLatLong(geo['lat'], geo['long'], api_key)


    forecast = {}

    # Get the forecast from the json
    for num, i in enumerate(data['daily']):
        forecast[num] = {
            "day": epoch_to_day_of_week(i['dt']),
            "datetime": epoch_to_datetime(i['dt']),
            "temp": round(i['temp']['day'], 0),
            "feels_like": i['feels_like']['day'] ,
            "max_temp": round(i['temp']['max'], 0),
            "min_temp": round(i['temp']['min'], 0),
            "humidity": i['humidity'],
            "uvi": i["uvi"],
            "wind_direction": i['wind_deg'],
            "wind_speed": i['wind_speed'],
            "wind_gust": i['wind_gust'],
            "weather": {
                "description": i['weather'][0]['description'],
                "icon": icon_url[0] + i['weather'][0]['icon'] + icon_url[1]
            }
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

    print(icon_url[0] + data['current']['weather'][0]['icon'] + icon_url[1])

    
    context = {}

    context['now'] = now
    context['forecast'] = forecast
    context['geo'] = geo
    
    # return "yay"
    return jsonify(context)
    # return forecast
    # return data