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

    fahrenheit = round( ((kelvin - 273.15) * 9/5 + 32), 2)
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
    data = {"alerts":[{"description":"* WHAT...Dangerous rip currents expected.\n\n* WHERE...Pinellas, Coastal Hillsborough, Coastal Manatee,\nCoastal Sarasota, Coastal Charlotte and Coastal Lee Counties.\n\n* WHEN...From 1 AM EST Wednesday through Wednesday evening.\n\n* IMPACTS...Rip currents can sweep even the best swimmers away\nfrom shore into deeper water.","end":1737590400,"event":"Rip Current Statement","sender_name":"NWS Tampa Bay Ruskin FL","start":1737525600,"tags":["Other dangers"]}],"current":{"clouds":100,"dew_point":38.41,"dt":1737565192,"feels_like":36.18,"humidity":91,"pressure":1027,"sunrise":1737548447,"sunset":1737586912,"temp":40.82,"uvi":2.83,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":20,"wind_gust":16.11,"wind_speed":6.91},"daily":[{"clouds":100,"dew_point":38.41,"dt":1737565200,"feels_like":{"day":32.54,"eve":49.6,"morn":35.22,"night":42.06},"humidity":91,"moon_phase":0.78,"moonrise":1737526440,"moonset":1737565980,"pop":1,"pressure":1027,"rain":4.69,"summary":"The day will start with rain through the late morning hours, transitioning to partly cloudy","sunrise":1737548447,"sunset":1737586912,"temp":{"day":40.82,"eve":51.64,"max":53.1,"min":40.82,"morn":42.46,"night":47.1},"uvi":4.1,"weather":[{"description":"moderate rain","icon":"10d","id":501,"main":"Rain"}],"wind_deg":23,"wind_gust":35.16,"wind_speed":21.36},{"clouds":100,"dew_point":41.74,"dt":1737651600,"feels_like":{"day":46,"eve":49.59,"morn":42.1,"night":45.18},"humidity":74,"moon_phase":0.81,"moonrise":1737616140,"moonset":1737654480,"pop":0,"pressure":1026,"summary":"There will be partly cloudy today","sunrise":1737634829,"sunset":1737673362,"temp":{"day":49.68,"eve":51.49,"max":51.87,"min":47.03,"morn":47.41,"night":49.42},"uvi":2.11,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":2,"wind_gust":15.55,"wind_speed":12.24},{"clouds":44,"dew_point":30.52,"dt":1737738000,"feels_like":{"day":47.8,"eve":43.25,"morn":39.36,"night":36},"humidity":46,"moon_phase":0.84,"moonrise":1737706020,"moonset":1737743340,"pop":0,"pressure":1026,"summary":"Expect a day of partly cloudy with clear spells","sunrise":1737721210,"sunset":1737759812,"temp":{"day":50.86,"eve":49.44,"max":52.68,"min":42.94,"morn":44.19,"night":42.94},"uvi":5.1,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":322,"wind_gust":24.09,"wind_speed":18.14},{"clouds":1,"dew_point":28.09,"dt":1737824400,"feels_like":{"day":47.37,"eve":51.58,"morn":30.27,"night":48.16},"humidity":41,"moon_phase":0.87,"moonrise":1737795960,"moonset":1737832620,"pop":0,"pressure":1032,"summary":"Expect a day of partly cloudy with clear spells","sunrise":1737807589,"sunset":1737846261,"temp":{"day":50.68,"eve":54.12,"max":58.21,"min":36.7,"morn":37.26,"night":50.32},"uvi":4.82,"weather":[{"description":"clear sky","icon":"01d","id":800,"main":"Clear"}],"wind_deg":14,"wind_gust":24.09,"wind_speed":13.13},{"clouds":87,"dew_point":48.43,"dt":1737910800,"feels_like":{"day":64.85,"eve":61.75,"morn":43.59,"night":57.67},"humidity":53,"moon_phase":0.9,"moonrise":1737885900,"moonset":1737922380,"pop":0,"pressure":1028,"summary":"You can expect partly cloudy in the morning, with clearing in the afternoon","sunrise":1737893967,"sunset":1737932711,"temp":{"day":66.06,"eve":62.85,"max":68.49,"min":47.73,"morn":47.73,"night":58.68},"uvi":5,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":60,"wind_gust":15.05,"wind_speed":9.01},{"clouds":40,"dew_point":52,"dt":1737997200,"feels_like":{"day":66.36,"eve":60.89,"morn":53.96,"night":58.35},"humidity":59,"moon_phase":0.94,"moonrise":1737975600,"moonset":1738012440,"pop":0,"pressure":1025,"summary":"There will be partly cloudy today","sunrise":1737980343,"sunset":1738019160,"temp":{"day":67.17,"eve":61.68,"max":67.91,"min":54.7,"morn":54.7,"night":59.07},"uvi":5,"weather":[{"description":"scattered clouds","icon":"03d","id":802,"main":"Clouds"}],"wind_deg":335,"wind_gust":12.73,"wind_speed":8.46},{"clouds":54,"dew_point":51.26,"dt":1738083600,"feels_like":{"day":66.92,"eve":62.8,"morn":54.14,"night":59.07},"humidity":56,"moon_phase":0.97,"moonrise":1738065060,"moonset":1738102800,"pop":0,"pressure":1022,"summary":"There will be partly cloudy today","sunrise":1738066718,"sunset":1738105610,"temp":{"day":67.8,"eve":63.68,"max":69.69,"min":54.7,"morn":54.7,"night":59.9},"uvi":5,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":346,"wind_gust":12.12,"wind_speed":8.23},{"clouds":96,"dew_point":46.99,"dt":1738170000,"feels_like":{"day":68.79,"eve":65.75,"morn":55.04,"night":61.77},"humidity":44,"moon_phase":0,"moonrise":1738154160,"moonset":1738193220,"pop":0,"pressure":1021,"summary":"There will be partly cloudy today","sunrise":1738153092,"sunset":1738192059,"temp":{"day":70.02,"eve":67.08,"max":72.37,"min":55.69,"morn":55.69,"night":63.09},"uvi":5,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":95,"wind_gust":17.49,"wind_speed":8.32}],"hourly":[{"clouds":98,"dew_point":38.1,"dt":1737561600,"feels_like":32.85,"humidity":88,"pop":0,"pressure":1027,"temp":41.38,"uvi":2.27,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":23,"wind_gust":20.96,"wind_speed":17.69},{"clouds":100,"dew_point":38.41,"dt":1737565200,"feels_like":32.54,"humidity":91,"pop":0,"pressure":1027,"temp":40.82,"uvi":2.83,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":25,"wind_gust":18.79,"wind_speed":16.22},{"clouds":98,"dew_point":38.43,"dt":1737568800,"feels_like":35.04,"humidity":86,"pop":0,"pressure":1027,"temp":42.31,"uvi":4.1,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":31,"wind_gust":16.11,"wind_speed":14.2},{"clouds":86,"dew_point":39.11,"dt":1737572400,"feels_like":38.53,"humidity":80,"pop":0,"pressure":1026,"temp":44.89,"uvi":3.55,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":36,"wind_gust":15.01,"wind_speed":13.49},{"clouds":74,"dew_point":40.01,"dt":1737576000,"feels_like":42.58,"humidity":74,"pop":0,"pressure":1025,"temp":47.88,"uvi":2.25,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":37,"wind_gust":14.18,"wind_speed":12.57},{"clouds":72,"dew_point":40.32,"dt":1737579600,"feels_like":48.79,"humidity":67,"pop":0,"pressure":1025,"temp":50.86,"uvi":0.99,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":40,"wind_gust":13.56,"wind_speed":12.17},{"clouds":74,"dew_point":40.24,"dt":1737583200,"feels_like":51.03,"humidity":62,"pop":0,"pressure":1024,"temp":53.1,"uvi":0.24,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":38,"wind_gust":13.67,"wind_speed":12.35},{"clouds":79,"dew_point":40.57,"dt":1737586800,"feels_like":49.6,"humidity":66,"pop":0,"pressure":1025,"temp":51.64,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":40,"wind_gust":15.55,"wind_speed":11.83},{"clouds":82,"dew_point":41.27,"dt":1737590400,"feels_like":48.22,"humidity":71,"pop":0,"pressure":1025,"temp":50.16,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":45,"wind_gust":16.24,"wind_speed":13.27},{"clouds":100,"dew_point":40.26,"dt":1737594000,"feels_like":43.2,"humidity":74,"pop":0,"pressure":1026,"temp":48.2,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":33,"wind_gust":17.67,"wind_speed":11.86},{"clouds":100,"dew_point":39.7,"dt":1737597600,"feels_like":42.37,"humidity":75,"pop":0,"pressure":1026,"temp":47.37,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":21,"wind_gust":18.3,"wind_speed":11.18},{"clouds":97,"dew_point":39.4,"dt":1737601200,"feels_like":41.74,"humidity":75,"pop":0,"pressure":1026,"temp":46.94,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":19,"wind_gust":18.84,"wind_speed":11.5},{"clouds":98,"dew_point":39.43,"dt":1737604800,"feels_like":42.06,"humidity":74,"pop":0,"pressure":1026,"temp":47.1,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":20,"wind_gust":16.42,"wind_speed":11.12},{"clouds":98,"dew_point":39.81,"dt":1737608400,"feels_like":42.66,"humidity":75,"pop":0,"pressure":1025,"temp":47.5,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":25,"wind_gust":14.34,"wind_speed":10.8},{"clouds":98,"dew_point":40.37,"dt":1737612000,"feels_like":43.29,"humidity":75,"pop":0,"pressure":1025,"temp":47.77,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":35,"wind_gust":13.4,"wind_speed":9.98},{"clouds":100,"dew_point":40.8,"dt":1737615600,"feels_like":43.32,"humidity":77,"pop":0,"pressure":1024,"temp":47.7,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":29,"wind_gust":13.04,"wind_speed":9.6},{"clouds":100,"dew_point":41.05,"dt":1737619200,"feels_like":43.39,"humidity":78,"pop":0,"pressure":1024,"temp":47.73,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":20,"wind_gust":12.59,"wind_speed":9.53},{"clouds":100,"dew_point":41.16,"dt":1737622800,"feels_like":43.72,"humidity":78,"pop":0,"pressure":1024,"temp":47.88,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":18,"wind_gust":11.77,"wind_speed":9.15},{"clouds":100,"dew_point":41.09,"dt":1737626400,"feels_like":43.11,"humidity":78,"pop":0,"pressure":1024,"temp":47.77,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":4,"wind_gust":12.84,"wind_speed":10.49},{"clouds":100,"dew_point":40.77,"dt":1737630000,"feels_like":42.1,"humidity":78,"pop":0,"pressure":1024,"temp":47.41,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":2,"wind_gust":15.55,"wind_speed":12.24},{"clouds":100,"dew_point":40.26,"dt":1737633600,"feels_like":42.17,"humidity":77,"pop":0,"pressure":1025,"temp":47.1,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":4,"wind_gust":14.7,"wind_speed":10.8},{"clouds":100,"dew_point":40.08,"dt":1737637200,"feels_like":43.48,"humidity":76,"pop":0,"pressure":1026,"temp":47.03,"uvi":0.11,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":6,"wind_gust":8.95,"wind_speed":7.27},{"clouds":100,"dew_point":40.26,"dt":1737640800,"feels_like":43.38,"humidity":76,"pop":0,"pressure":1026,"temp":47.39,"uvi":0.33,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":3,"wind_gust":9.95,"wind_speed":8.52},{"clouds":100,"dew_point":40.66,"dt":1737644400,"feels_like":43.88,"humidity":75,"pop":0,"pressure":1026,"temp":48.11,"uvi":0.77,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":6,"wind_gust":11.43,"wind_speed":9.51},{"clouds":100,"dew_point":41.14,"dt":1737648000,"feels_like":45.1,"humidity":74,"pop":0,"pressure":1026,"temp":49.12,"uvi":1.4,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":7,"wind_gust":11.3,"wind_speed":9.55},{"clouds":100,"dew_point":41.74,"dt":1737651600,"feels_like":46,"humidity":74,"pop":0,"pressure":1026,"temp":49.68,"uvi":2.11,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":10,"wind_gust":10.4,"wind_speed":8.97},{"clouds":100,"dew_point":42.08,"dt":1737655200,"feels_like":48.49,"humidity":73,"pop":0,"pressure":1025,"temp":50.32,"uvi":1.95,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":3,"wind_gust":10.67,"wind_speed":9.1},{"clouds":100,"dew_point":41.97,"dt":1737658800,"feels_like":48.85,"humidity":72,"pop":0,"pressure":1024,"temp":50.7,"uvi":1.05,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":357,"wind_gust":10.58,"wind_speed":9.01},{"clouds":100,"dew_point":42.12,"dt":1737662400,"feels_like":49.39,"humidity":71,"pop":0,"pressure":1023,"temp":51.22,"uvi":0.89,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":352,"wind_gust":11.21,"wind_speed":9.46},{"clouds":100,"dew_point":41.94,"dt":1737666000,"feels_like":50,"humidity":69,"pop":0,"pressure":1023,"temp":51.87,"uvi":0.44,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":351,"wind_gust":10.56,"wind_speed":9.19},{"clouds":100,"dew_point":41.86,"dt":1737669600,"feels_like":49.86,"humidity":69,"pop":0,"pressure":1023,"temp":51.75,"uvi":0.12,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":348,"wind_gust":10.11,"wind_speed":8.95},{"clouds":100,"dew_point":41.79,"dt":1737673200,"feels_like":49.59,"humidity":69,"pop":0,"pressure":1024,"temp":51.49,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":344,"wind_gust":11.12,"wind_speed":9.26},{"clouds":100,"dew_point":42.24,"dt":1737676800,"feels_like":49.3,"humidity":71,"pop":0,"pressure":1025,"temp":51.15,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":340,"wind_gust":13.42,"wind_speed":10.89},{"clouds":100,"dew_point":42.66,"dt":1737680400,"feels_like":49.06,"humidity":73,"pop":0,"pressure":1025,"temp":50.85,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":343,"wind_gust":13.76,"wind_speed":10.22},{"clouds":100,"dew_point":42.78,"dt":1737684000,"feels_like":49.24,"humidity":73,"pop":0,"pressure":1025,"temp":51.01,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":348,"wind_gust":12.03,"wind_speed":8.39},{"clouds":100,"dew_point":42.04,"dt":1737687600,"feels_like":49.03,"humidity":72,"pop":0,"pressure":1025,"temp":50.86,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":357,"wind_gust":11.21,"wind_speed":9.01},{"clouds":100,"dew_point":41.23,"dt":1737691200,"feels_like":45.18,"humidity":73,"pop":0,"pressure":1025,"temp":49.42,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":5,"wind_gust":10.78,"wind_speed":10.42},{"clouds":98,"dew_point":40.75,"dt":1737694800,"feels_like":41.83,"humidity":79,"pop":0,"pressure":1024,"temp":46.9,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":2,"wind_gust":12.55,"wind_speed":11.07},{"clouds":96,"dew_point":40.06,"dt":1737698400,"feels_like":40.66,"humidity":81,"pop":0,"pressure":1024,"temp":45.72,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":2,"wind_gust":12.03,"wind_speed":10.2},{"clouds":90,"dew_point":39.83,"dt":1737702000,"feels_like":40.86,"humidity":80,"pop":0,"pressure":1024,"temp":45.7,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":1,"wind_gust":11.27,"wind_speed":9.62},{"clouds":79,"dew_point":39.49,"dt":1737705600,"feels_like":39.88,"humidity":81,"pop":0,"pressure":1023,"temp":44.91,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":353,"wind_gust":11.25,"wind_speed":9.6},{"clouds":78,"dew_point":39.06,"dt":1737709200,"feels_like":38.8,"humidity":83,"pop":0,"pressure":1023,"temp":43.75,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":354,"wind_gust":10.96,"wind_speed":8.77},{"clouds":80,"dew_point":38.77,"dt":1737712800,"feels_like":38.97,"humidity":83,"pop":0,"pressure":1024,"temp":43.63,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":357,"wind_gust":10.47,"wind_speed":8.1},{"clouds":84,"dew_point":38.77,"dt":1737716400,"feels_like":39.36,"humidity":81,"pop":0,"pressure":1024,"temp":44.19,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":357,"wind_gust":11.1,"wind_speed":8.7},{"clouds":87,"dew_point":38.39,"dt":1737720000,"feels_like":39.25,"humidity":79,"pop":0,"pressure":1025,"temp":44.47,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":356,"wind_gust":12.35,"wind_speed":9.84},{"clouds":100,"dew_point":36.21,"dt":1737723600,"feels_like":38.62,"humidity":73,"pop":0,"pressure":1025,"temp":44.29,"uvi":0.22,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":353,"wind_gust":13.53,"wind_speed":10.89},{"clouds":100,"dew_point":33.06,"dt":1737727200,"feels_like":38.98,"humidity":64,"pop":0,"pressure":1026,"temp":44.71,"uvi":1.11,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":351,"wind_gust":13.09,"wind_speed":11.36},{"clouds":73,"dew_point":31.5,"dt":1737730800,"feels_like":41.29,"humidity":56,"pop":0,"pressure":1026,"temp":46.53,"uvi":2.56,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":346,"wind_gust":12.24,"wind_speed":11.27}],"lat":27.9478,"lon":-82.4584,"minutely":[{"dt":1737565200,"precipitation":0},{"dt":1737565260,"precipitation":0},{"dt":1737565320,"precipitation":0},{"dt":1737565380,"precipitation":0},{"dt":1737565440,"precipitation":0},{"dt":1737565500,"precipitation":0},{"dt":1737565560,"precipitation":0},{"dt":1737565620,"precipitation":0},{"dt":1737565680,"precipitation":0},{"dt":1737565740,"precipitation":0},{"dt":1737565800,"precipitation":0},{"dt":1737565860,"precipitation":0},{"dt":1737565920,"precipitation":0},{"dt":1737565980,"precipitation":0},{"dt":1737566040,"precipitation":0},{"dt":1737566100,"precipitation":0},{"dt":1737566160,"precipitation":0},{"dt":1737566220,"precipitation":0},{"dt":1737566280,"precipitation":0},{"dt":1737566340,"precipitation":0},{"dt":1737566400,"precipitation":0},{"dt":1737566460,"precipitation":0},{"dt":1737566520,"precipitation":0},{"dt":1737566580,"precipitation":0},{"dt":1737566640,"precipitation":0},{"dt":1737566700,"precipitation":0},{"dt":1737566760,"precipitation":0},{"dt":1737566820,"precipitation":0},{"dt":1737566880,"precipitation":0},{"dt":1737566940,"precipitation":0},{"dt":1737567000,"precipitation":0},{"dt":1737567060,"precipitation":0},{"dt":1737567120,"precipitation":0},{"dt":1737567180,"precipitation":0},{"dt":1737567240,"precipitation":0},{"dt":1737567300,"precipitation":0},{"dt":1737567360,"precipitation":0},{"dt":1737567420,"precipitation":0},{"dt":1737567480,"precipitation":0},{"dt":1737567540,"precipitation":0},{"dt":1737567600,"precipitation":0},{"dt":1737567660,"precipitation":0},{"dt":1737567720,"precipitation":0},{"dt":1737567780,"precipitation":0},{"dt":1737567840,"precipitation":0},{"dt":1737567900,"precipitation":0},{"dt":1737567960,"precipitation":0},{"dt":1737568020,"precipitation":0},{"dt":1737568080,"precipitation":0},{"dt":1737568140,"precipitation":0},{"dt":1737568200,"precipitation":0},{"dt":1737568260,"precipitation":0},{"dt":1737568320,"precipitation":0},{"dt":1737568380,"precipitation":0},{"dt":1737568440,"precipitation":0},{"dt":1737568500,"precipitation":0},{"dt":1737568560,"precipitation":0},{"dt":1737568620,"precipitation":0},{"dt":1737568680,"precipitation":0},{"dt":1737568740,"precipitation":0}],"timezone":"America/New_York","timezone_offset":-18000}




    load_dotenv()
    api_key = os.getenv('API_KEY')

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
            "temp": i['temp']['day'],
            "feels_like": i['feels_like']['day'] ,
            "max_temp": i['temp']['max'],
            "min_temp": i['temp']['min'],
            "humidity": i['humidity'],
            "uvi": i["uvi"],
            "wind_direction": i['wind_deg'],
            "wind_speed": i['wind_speed'],
            "wind_gust": i['wind_gust'],
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
        "temp": data['current']['temp'],
        "feels_like": data['current']['feels_like'],
        "humidity": data['current']['humidity'],
        "uvi": data['current']["uvi"],
        "wind_direction": data['current']['wind_deg'],
        "wind_speed": data['current']['wind_speed'],
        "timestamp": epoch_to_datetime(data['current']['dt'])
    }

    
    context = {}

    context['now'] = now
    context['forecast'] = forecast
    context['geo'] = geo
    
    # return "yay"
    return jsonify(context)
    # return forecast
    # return data