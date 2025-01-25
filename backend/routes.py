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
    data = {"current":{"clouds":40,"dew_point":28.4,"dt":1737735641,"feels_like":42.3,"humidity":47,"pressure":1027,"sunrise":1737721210,"sunset":1737759812,"temp":47.08,"uvi":4.05,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":360,"wind_speed":10.36},"daily":[{"clouds":32,"dew_point":27.21,"dt":1737738000,"feels_like":{"day":43.07,"eve":48.24,"morn":36.95,"night":39.97},"humidity":43,"moon_phase":0.84,"moonrise":1737706020,"moonset":1737743340,"pop":0,"pressure":1027,"summary":"You can expect partly cloudy in the morning, with clearing in the afternoon","sunrise":1737721210,"sunset":1737759812,"temp":{"day":47.98,"eve":51.58,"max":54.95,"min":42.28,"morn":42.73,"night":45.7},"uvi":4.99,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":338,"wind_gust":23.35,"wind_speed":15.32},{"clouds":1,"dew_point":32.43,"dt":1737824400,"feels_like":{"day":51.85,"eve":55.36,"morn":33.28,"night":49.41},"humidity":43,"moon_phase":0.87,"moonrise":1737795960,"moonset":1737832620,"pop":0,"pressure":1031,"summary":"Expect a day of partly cloudy with clear spells","sunrise":1737807589,"sunset":1737846261,"temp":{"day":54.66,"eve":57.69,"max":60.35,"min":39.36,"morn":39.87,"night":51.33},"uvi":4.84,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":7,"wind_gust":23.15,"wind_speed":11.95},{"clouds":99,"dew_point":46.27,"dt":1737910800,"feels_like":{"day":59.95,"eve":61.93,"morn":45.77,"night":55},"humidity":58,"moon_phase":0.9,"moonrise":1737885900,"moonset":1737922380,"pop":0,"pressure":1029,"summary":"Expect a day of partly cloudy with clear spells","sunrise":1737893967,"sunset":1737932711,"temp":{"day":61.39,"eve":63.32,"max":65.95,"min":48.67,"morn":49.14,"night":56.12},"uvi":4.87,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":43,"wind_gust":18.37,"wind_speed":9.82},{"clouds":63,"dew_point":49.19,"dt":1737997200,"feels_like":{"day":64.29,"eve":59.59,"morn":52.11,"night":56.97},"humidity":57,"moon_phase":0.94,"moonrise":1737975600,"moonset":1738012440,"pop":0,"pressure":1024,"summary":"You can expect partly cloudy in the morning, with clearing in the afternoon","sunrise":1737980343,"sunset":1738019160,"temp":{"day":65.37,"eve":60.67,"max":65.93,"min":52.97,"morn":53.15,"night":58.03},"uvi":4.57,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":326,"wind_gust":14.54,"wind_speed":8.34},{"clouds":9,"dew_point":53.1,"dt":1738083600,"feels_like":{"day":66.11,"eve":61.83,"morn":54.45,"night":59.59},"humidity":62,"moon_phase":0.97,"moonrise":1738065060,"moonset":1738102800,"pop":0,"pressure":1020,"summary":"Expect a day of partly cloudy with clear spells","sunrise":1738066718,"sunset":1738105610,"temp":{"day":66.81,"eve":62.37,"max":67.01,"min":55.09,"morn":55.09,"night":59.95},"uvi":5,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":294,"wind_gust":8.48,"wind_speed":8.05},{"clouds":100,"dew_point":52.61,"dt":1738170000,"feels_like":{"day":66.06,"eve":62.2,"morn":56.93,"night":60.84},"humidity":61,"moon_phase":0,"moonrise":1738154160,"moonset":1738193220,"pop":0,"pressure":1019,"summary":"There will be partly cloudy today","sunrise":1738153092,"sunset":1738192059,"temp":{"day":66.81,"eve":63.05,"max":67.3,"min":57.24,"morn":57.24,"night":61.56},"uvi":5,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":233,"wind_gust":9.26,"wind_speed":6.8},{"clouds":40,"dew_point":51.24,"dt":1738256400,"feels_like":{"day":70.12,"eve":66.74,"morn":57.67,"night":63.57},"humidity":51,"moon_phase":0.04,"moonrise":1738242960,"moonset":1738283640,"pop":0,"pressure":1021,"summary":"There will be partly cloudy today","sunrise":1738239464,"sunset":1738278508,"temp":{"day":70.93,"eve":67.42,"max":71.98,"min":58.06,"morn":58.06,"night":64.13},"uvi":5,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":338,"wind_gust":14.52,"wind_speed":8.16},{"clouds":100,"dew_point":56.82,"dt":1738342800,"feels_like":{"day":71.01,"eve":63.72,"morn":58.01,"night":65.97},"humidity":60,"moon_phase":0.08,"moonrise":1738331520,"moonset":1738373940,"pop":0,"pressure":1024,"summary":"There will be partly cloudy today","sunrise":1738325834,"sunset":1738364957,"temp":{"day":71.35,"eve":63.91,"max":71.35,"min":58.08,"morn":58.08,"night":65.91},"uvi":5,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":48,"wind_gust":32.03,"wind_speed":20.36}],"hourly":[{"clouds":40,"dew_point":28.4,"dt":1737734400,"feels_like":41.83,"humidity":47,"pop":0,"pressure":1027,"temp":47.08,"uvi":4.05,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":23,"wind_gust":15.26,"wind_speed":11.74},{"clouds":32,"dew_point":27.21,"dt":1737738000,"feels_like":43.07,"humidity":43,"pop":0,"pressure":1027,"temp":47.98,"uvi":4.99,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":6,"wind_gust":14.07,"wind_speed":11.39},{"clouds":24,"dew_point":26.06,"dt":1737741600,"feels_like":45.18,"humidity":38,"pop":0,"pressure":1027,"temp":49.86,"uvi":4.99,"visibility":10000,"weather":[{"description":"few clouds","icon":"02d","id":801,"main":"Clouds"}],"wind_deg":353,"wind_gust":14.7,"wind_speed":12.24},{"clouds":16,"dew_point":25.41,"dt":1737745200,"feels_like":48.54,"humidity":34,"pop":0,"pressure":1026,"temp":52.03,"uvi":4.02,"visibility":10000,"weather":[{"description":"few clouds","icon":"02d","id":801,"main":"Clouds"}],"wind_deg":349,"wind_gust":15.82,"wind_speed":13.35},{"clouds":8,"dew_point":24.96,"dt":1737748800,"feels_like":50.52,"humidity":31,"pop":0,"pressure":1025,"temp":53.96,"uvi":2.48,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":338,"wind_gust":17.65,"wind_speed":15.32},{"clouds":0,"dew_point":23.31,"dt":1737752400,"feels_like":51.51,"humidity":29,"pop":0,"pressure":1026,"temp":54.95,"uvi":1.08,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":335,"wind_gust":17.45,"wind_speed":15.01},{"clouds":1,"dew_point":25.63,"dt":1737756000,"feels_like":50.34,"humidity":34,"pop":0,"pressure":1027,"temp":53.67,"uvi":0.26,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":331,"wind_gust":17.47,"wind_speed":14.43},{"clouds":2,"dew_point":26.58,"dt":1737759600,"feels_like":48.24,"humidity":38,"pop":0,"pressure":1027,"temp":51.58,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":335,"wind_gust":16.98,"wind_speed":12.08},{"clouds":6,"dew_point":28.6,"dt":1737763200,"feels_like":47.34,"humidity":43,"pop":0,"pressure":1028,"temp":50.56,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":325,"wind_gust":20.51,"wind_speed":13.42},{"clouds":7,"dew_point":31.46,"dt":1737766800,"feels_like":47.1,"humidity":48,"pop":0,"pressure":1029,"temp":50.13,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":335,"wind_gust":22.17,"wind_speed":13.42},{"clouds":3,"dew_point":30.02,"dt":1737770400,"feels_like":44.37,"humidity":48,"pop":0,"pressure":1029,"temp":49.06,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":6,"wind_gust":21.23,"wind_speed":11.59},{"clouds":2,"dew_point":24.26,"dt":1737774000,"feels_like":41.67,"humidity":40,"pop":0,"pressure":1029,"temp":47.23,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":13,"wind_gust":23.35,"wind_speed":12.91},{"clouds":2,"dew_point":24.28,"dt":1737777600,"feels_like":39.97,"humidity":43,"pop":0,"pressure":1030,"temp":45.7,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":8,"wind_gust":23.29,"wind_speed":12.1},{"clouds":3,"dew_point":24.73,"dt":1737781200,"feels_like":38.55,"humidity":45,"pop":0,"pressure":1030,"temp":44.53,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":7,"wind_gust":23.15,"wind_speed":11.95},{"clouds":3,"dew_point":25.59,"dt":1737784800,"feels_like":37.74,"humidity":49,"pop":0,"pressure":1030,"temp":43.5,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":13,"wind_gust":21.3,"wind_speed":10.6},{"clouds":5,"dew_point":26.42,"dt":1737788400,"feels_like":36.68,"humidity":52,"pop":0,"pressure":1030,"temp":42.57,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":16,"wind_gust":20.42,"wind_speed":10.38},{"clouds":4,"dew_point":26.65,"dt":1737792000,"feels_like":35.67,"humidity":54,"pop":0,"pressure":1030,"temp":41.77,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":18,"wind_gust":20.33,"wind_speed":10.4},{"clouds":3,"dew_point":26.83,"dt":1737795600,"feels_like":34.86,"humidity":57,"pop":0,"pressure":1030,"temp":41.07,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":20,"wind_gust":20.2,"wind_speed":10.25},{"clouds":3,"dew_point":26.96,"dt":1737799200,"feels_like":34.09,"humidity":58,"pop":0,"pressure":1030,"temp":40.42,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":26,"wind_gust":20.11,"wind_speed":10.2},{"clouds":3,"dew_point":26.78,"dt":1737802800,"feels_like":33.28,"humidity":59,"pop":0,"pressure":1030,"temp":39.87,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":32,"wind_gust":20.51,"wind_speed":10.47},{"clouds":2,"dew_point":26.6,"dt":1737806400,"feels_like":32.92,"humidity":60,"pop":0,"pressure":1031,"temp":39.36,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":41,"wind_gust":20.8,"wind_speed":9.84},{"clouds":3,"dew_point":26.69,"dt":1737810000,"feels_like":33.35,"humidity":59,"pop":0,"pressure":1031,"temp":39.72,"uvi":0.27,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":41,"wind_gust":20.85,"wind_speed":9.89},{"clouds":2,"dew_point":26.92,"dt":1737813600,"feels_like":36.73,"humidity":53,"pop":0,"pressure":1031,"temp":43.07,"uvi":1.09,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":46,"wind_gust":19.89,"wind_speed":11.92},{"clouds":2,"dew_point":29.62,"dt":1737817200,"feels_like":42.19,"humidity":50,"pop":0,"pressure":1032,"temp":47.35,"uvi":2.45,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":53,"wind_gust":17.47,"wind_speed":11.68},{"clouds":2,"dew_point":31.51,"dt":1737820800,"feels_like":48.27,"humidity":47,"pop":0,"pressure":1031,"temp":51.24,"uvi":3.91,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":59,"wind_gust":15.37,"wind_speed":11.32},{"clouds":1,"dew_point":32.43,"dt":1737824400,"feels_like":51.85,"humidity":43,"pop":0,"pressure":1031,"temp":54.66,"uvi":4.84,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":62,"wind_gust":14.07,"wind_speed":10.49},{"clouds":2,"dew_point":33.13,"dt":1737828000,"feels_like":54.37,"humidity":40,"pop":0,"pressure":1030,"temp":57.09,"uvi":4.83,"visibility":10000,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":64,"wind_gust":12.39,"wind_speed":9.01},{"clouds":33,"dew_point":33.76,"dt":1737831600,"feels_like":56.21,"humidity":39,"pop":0,"pressure":1029,"temp":58.8,"uvi":3.89,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":63,"wind_gust":11.14,"wind_speed":8.1},{"clouds":65,"dew_point":34.65,"dt":1737835200,"feels_like":57.33,"humidity":39,"pop":0,"pressure":1028,"temp":59.81,"uvi":2.42,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":62,"wind_gust":10.71,"wind_speed":8.14},{"clouds":53,"dew_point":35.62,"dt":1737838800,"feels_like":57.97,"humidity":40,"pop":0,"pressure":1028,"temp":60.35,"uvi":1.06,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":60,"wind_gust":11.01,"wind_speed":8.55},{"clouds":42,"dew_point":37.08,"dt":1737842400,"feels_like":57.78,"humidity":42,"pop":0,"pressure":1028,"temp":60.1,"uvi":0.26,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":55,"wind_gust":11.65,"wind_speed":8.25},{"clouds":33,"dew_point":37.85,"dt":1737846000,"feels_like":55.36,"humidity":47,"pop":0,"pressure":1028,"temp":57.69,"uvi":0,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":28,"wind_gust":9.57,"wind_speed":7.02},{"clouds":27,"dew_point":37.51,"dt":1737849600,"feels_like":53.58,"humidity":50,"pop":0,"pressure":1029,"temp":55.94,"uvi":0,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03n","id":802,"main":"Clouds"}],"wind_deg":22,"wind_gust":11.43,"wind_speed":7.99},{"clouds":0,"dew_point":38.1,"dt":1737853200,"feels_like":52.11,"humidity":54,"pop":0,"pressure":1030,"temp":54.43,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":34,"wind_gust":13.51,"wind_speed":8.14},{"clouds":0,"dew_point":39.34,"dt":1737856800,"feels_like":51.03,"humidity":59,"pop":0,"pressure":1030,"temp":53.22,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":43,"wind_gust":13.76,"wind_speed":7.76},{"clouds":0,"dew_point":40.69,"dt":1737860400,"feels_like":50.07,"humidity":65,"pop":0,"pressure":1030,"temp":52.11,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":58,"wind_gust":17.67,"wind_speed":8.52},{"clouds":1,"dew_point":41.61,"dt":1737864000,"feels_like":49.41,"humidity":69,"pop":0,"pressure":1030,"temp":51.33,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":60,"wind_gust":17.83,"wind_speed":8.19},{"clouds":9,"dew_point":41.59,"dt":1737867600,"feels_like":48.72,"humidity":71,"pop":0,"pressure":1029,"temp":50.63,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":54,"wind_gust":14.5,"wind_speed":7.58},{"clouds":18,"dew_point":41.52,"dt":1737871200,"feels_like":48.16,"humidity":72,"pop":0,"pressure":1029,"temp":50.07,"uvi":0,"visibility":10000,"weather":[{"description":"few clouds","icon":"02n","id":801,"main":"Clouds"}],"wind_deg":53,"wind_gust":13.91,"wind_speed":7.18},{"clouds":99,"dew_point":41.31,"dt":1737874800,"feels_like":46.85,"humidity":73,"pop":0,"pressure":1029,"temp":49.84,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":51,"wind_gust":13.27,"wind_speed":7.31},{"clouds":99,"dew_point":41.45,"dt":1737878400,"feels_like":46.78,"humidity":73,"pop":0,"pressure":1029,"temp":49.53,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":44,"wind_gust":11.1,"wind_speed":6.67},{"clouds":100,"dew_point":41.45,"dt":1737882000,"feels_like":45.99,"humidity":75,"pop":0,"pressure":1029,"temp":49.17,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":46,"wind_gust":11.9,"wind_speed":7.47},{"clouds":100,"dew_point":41.63,"dt":1737885600,"feels_like":45.55,"humidity":76,"pop":0,"pressure":1029,"temp":48.87,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":37,"wind_gust":12.01,"wind_speed":7.61},{"clouds":100,"dew_point":41.83,"dt":1737889200,"feels_like":45.77,"humidity":76,"pop":0,"pressure":1029,"temp":49.14,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":33,"wind_gust":13.18,"wind_speed":7.85},{"clouds":100,"dew_point":41.85,"dt":1737892800,"feels_like":45,"humidity":77,"pop":0,"pressure":1030,"temp":48.67,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":36,"wind_gust":14.63,"wind_speed":8.34},{"clouds":100,"dew_point":41.95,"dt":1737896400,"feels_like":45.12,"humidity":77,"pop":0,"pressure":1030,"temp":48.9,"uvi":0.27,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":41,"wind_gust":16.28,"wind_speed":8.77},{"clouds":100,"dew_point":42.55,"dt":1737900000,"feels_like":49.5,"humidity":72,"pop":0,"pressure":1030,"temp":51.28,"uvi":1.06,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":43,"wind_gust":15.66,"wind_speed":9.82},{"clouds":100,"dew_point":43.84,"dt":1737903600,"feels_like":53.49,"humidity":66,"pop":0,"pressure":1030,"temp":55.17,"uvi":2.33,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":52,"wind_gust":13.51,"wind_speed":9.46}],"lat":27.9478,"lon":-82.4584,"minutely":[{"dt":1737735660,"precipitation":0},{"dt":1737735720,"precipitation":0},{"dt":1737735780,"precipitation":0},{"dt":1737735840,"precipitation":0},{"dt":1737735900,"precipitation":0},{"dt":1737735960,"precipitation":0},{"dt":1737736020,"precipitation":0},{"dt":1737736080,"precipitation":0},{"dt":1737736140,"precipitation":0},{"dt":1737736200,"precipitation":0},{"dt":1737736260,"precipitation":0},{"dt":1737736320,"precipitation":0},{"dt":1737736380,"precipitation":0},{"dt":1737736440,"precipitation":0},{"dt":1737736500,"precipitation":0},{"dt":1737736560,"precipitation":0},{"dt":1737736620,"precipitation":0},{"dt":1737736680,"precipitation":0},{"dt":1737736740,"precipitation":0},{"dt":1737736800,"precipitation":0},{"dt":1737736860,"precipitation":0},{"dt":1737736920,"precipitation":0},{"dt":1737736980,"precipitation":0},{"dt":1737737040,"precipitation":0},{"dt":1737737100,"precipitation":0},{"dt":1737737160,"precipitation":0},{"dt":1737737220,"precipitation":0},{"dt":1737737280,"precipitation":0},{"dt":1737737340,"precipitation":0},{"dt":1737737400,"precipitation":0},{"dt":1737737460,"precipitation":0},{"dt":1737737520,"precipitation":0},{"dt":1737737580,"precipitation":0},{"dt":1737737640,"precipitation":0},{"dt":1737737700,"precipitation":0},{"dt":1737737760,"precipitation":0},{"dt":1737737820,"precipitation":0},{"dt":1737737880,"precipitation":0},{"dt":1737737940,"precipitation":0},{"dt":1737738000,"precipitation":0},{"dt":1737738060,"precipitation":0},{"dt":1737738120,"precipitation":0},{"dt":1737738180,"precipitation":0},{"dt":1737738240,"precipitation":0},{"dt":1737738300,"precipitation":0},{"dt":1737738360,"precipitation":0},{"dt":1737738420,"precipitation":0},{"dt":1737738480,"precipitation":0},{"dt":1737738540,"precipitation":0},{"dt":1737738600,"precipitation":0},{"dt":1737738660,"precipitation":0},{"dt":1737738720,"precipitation":0},{"dt":1737738780,"precipitation":0},{"dt":1737738840,"precipitation":0},{"dt":1737738900,"precipitation":0},{"dt":1737738960,"precipitation":0},{"dt":1737739020,"precipitation":0},{"dt":1737739080,"precipitation":0},{"dt":1737739140,"precipitation":0},{"dt":1737739200,"precipitation":0}],"timezone":"America/New_York","timezone_offset":-18000}





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