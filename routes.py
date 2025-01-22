from app import app

import random, requests, json, time, pandas as pd, numpy as np 
from datetime import datetime

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



def getLatLongByCity(cityName):
    API_Key = ""
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={cityName}&appid={API_Key}"
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


def getDataWLatLong(lat, long):

    API_Key = ""
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid={API_Key}"
    response = requests.get(url)
    data = response.json()

    return data



@app.route('/')
def index():
    
    
    lat = 27.9574621
    long = -82.4597585

    # https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API key}

    # This url is used to get lat and long coords by city name
    # http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}


    # url = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(lat)+"&lon="+str(long)+"&appid="+API_Key

    

    # Offline data
    geo = {"city":"Tampa","country":"US","lat":27.9477595,"long":-82.458444,"state":"Florida"}
    data = {"current":{"clouds":100,"dew_point":274.52,"dt":1737523395,"feels_like":275.84,"humidity":91,"pressure":1005,"sunrise":1737532335,"sunset":1737563496,"temp":275.84,"uvi":0,"visibility":3800,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":0,"wind_speed":1.03},"daily":[{"clouds":100,"dew_point":275.57,"dt":1737547200,"feels_like":{"day":275.6,"eve":274.89,"morn":274.75,"night":275.73},"humidity":91,"moon_phase":0.77,"moonrise":1737508980,"moonset":1737542340,"pop":1,"pressure":1003,"rain":0.79,"summary":"Expect a day of partly cloudy with rain","sunrise":1737532335,"sunset":1737563496,"temp":{"day":276.99,"eve":276.32,"max":277.26,"min":275.4,"morn":275.99,"night":275.73},"uvi":0.1,"weather":[{"description":"light rain","icon":"10d","id":500,"main":"Rain"}],"wind_deg":336,"wind_gust":5.81,"wind_speed":2.14},{"clouds":81,"dew_point":277.21,"dt":1737633600,"feels_like":{"day":276.74,"eve":275.82,"morn":271.84,"night":275.21},"humidity":82,"moon_phase":0.8,"moonrise":1737599760,"moonset":1737629760,"pop":1,"pressure":1002,"rain":4.33,"summary":"Expect a day of partly cloudy with rain","sunrise":1737618665,"sunset":1737649999,"temp":{"day":280.21,"eve":279.38,"max":280.9,"min":274.66,"morn":274.72,"night":278.45},"uvi":0.39,"weather":[{"description":"moderate rain","icon":"10d","id":501,"main":"Rain"}],"wind_deg":237,"wind_gust":16.75,"wind_speed":8.04},{"clouds":100,"dew_point":276.23,"dt":1737720000,"feels_like":{"day":279.23,"eve":276.2,"morn":278.18,"night":276.52},"humidity":65,"moon_phase":0.83,"moonrise":1737690720,"moonset":1737717540,"pop":1,"pressure":995,"rain":7.72,"summary":"Expect a day of partly cloudy with rain","sunrise":1737704991,"sunset":1737736503,"temp":{"day":282.56,"eve":279.71,"max":283.67,"min":278.75,"morn":282.37,"night":278.75},"uvi":0.65,"weather":[{"description":"moderate rain","icon":"10d","id":501,"main":"Rain"}],"wind_deg":202,"wind_gust":26.08,"wind_speed":10.9},{"clouds":100,"dew_point":274.62,"dt":1737806400,"feels_like":{"day":276.07,"eve":274.99,"morn":278.04,"night":274.45},"humidity":79,"moon_phase":0.86,"moonrise":1737781560,"moonset":1737805920,"pop":0.89,"pressure":1006,"rain":1.15,"summary":"Expect a day of partly cloudy with rain","sunrise":1737791316,"sunset":1737823008,"temp":{"day":278.06,"eve":277.66,"max":279.31,"min":277.31,"morn":278.04,"night":277.48},"uvi":0.35,"weather":[{"description":"light rain","icon":"10d","id":500,"main":"Rain"}],"wind_deg":185,"wind_gust":12.01,"wind_speed":3.57},{"clouds":64,"dew_point":276.5,"dt":1737892800,"feels_like":{"day":278.28,"eve":274.55,"morn":275.53,"night":274.27},"humidity":73,"moon_phase":0.89,"moonrise":1737871920,"moonset":1737895140,"pop":0.2,"pressure":1006,"rain":0.14,"summary":"Expect a day of partly cloudy with rain","sunrise":1737877638,"sunset":1737909514,"temp":{"day":281.09,"eve":278.25,"max":281.09,"min":278.24,"morn":279.15,"night":278.24},"uvi":0.74,"weather":[{"description":"light rain","icon":"10d","id":500,"main":"Rain"}],"wind_deg":197,"wind_gust":13.79,"wind_speed":6.42},{"clouds":83,"dew_point":277.74,"dt":1737979200,"feels_like":{"day":277.76,"eve":276.61,"morn":277.74,"night":278.39},"humidity":81,"moon_phase":0.93,"moonrise":1737961560,"moonset":1737985500,"pop":1,"pressure":993,"rain":8.82,"summary":"Expect a day of partly cloudy with rain","sunrise":1737963958,"sunset":1737996020,"temp":{"day":280.87,"eve":280.68,"max":282.04,"min":278.51,"morn":280.03,"night":282.04},"uvi":1,"weather":[{"description":"moderate rain","icon":"10d","id":501,"main":"Rain"}],"wind_deg":127,"wind_gust":19.65,"wind_speed":8.02},{"clouds":100,"dew_point":279.92,"dt":1738065600,"feels_like":{"day":282.98,"eve":279.51,"morn":282.41,"night":278.81},"humidity":77,"moon_phase":0.96,"moonrise":1738050360,"moonset":1738076700,"pop":1,"pressure":984,"rain":6.51,"summary":"Expect a day of partly cloudy with rain","sunrise":1738050276,"sunset":1738082527,"temp":{"day":283.84,"eve":282.8,"max":283.84,"min":282.18,"morn":283.18,"night":282.18},"uvi":1,"weather":[{"description":"moderate rain","icon":"10d","id":501,"main":"Rain"}],"wind_deg":167,"wind_gust":16.77,"wind_speed":8.36},{"clouds":100,"dew_point":278.9,"dt":1738152000,"feels_like":{"day":277.94,"eve":279.53,"morn":276.21,"night":279.52},"humidity":84,"moon_phase":0,"moonrise":1738138380,"moonset":1738168320,"pop":1,"pressure":994,"rain":9.06,"summary":"Expect a day of partly cloudy with rain","sunrise":1738136591,"sunset":1738169034,"temp":{"day":281.59,"eve":282.39,"max":282.39,"min":280.44,"morn":280.44,"night":282.28},"uvi":1,"weather":[{"description":"moderate rain","icon":"10d","id":501,"main":"Rain"}],"wind_deg":201,"wind_gust":17.07,"wind_speed":8.8}],"hourly":[{"clouds":100,"dew_point":274.52,"dt":1737522000,"feels_like":275.84,"humidity":91,"pop":0.2,"pressure":1005,"rain":{"1h":0.32},"temp":275.84,"uvi":0,"visibility":10000,"weather":[{"description":"light rain","icon":"10n","id":500,"main":"Rain"}],"wind_deg":57,"wind_gust":2.63,"wind_speed":1.32},{"clouds":100,"dew_point":274.82,"dt":1737525600,"feels_like":274.75,"humidity":92,"pop":0.8,"pressure":1005,"temp":275.99,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":49,"wind_gust":3.06,"wind_speed":1.42},{"clouds":100,"dew_point":275.12,"dt":1737529200,"feels_like":276.14,"humidity":93,"pop":0.8,"pressure":1005,"temp":276.14,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":29,"wind_gust":2.78,"wind_speed":1.32},{"clouds":100,"dew_point":275.45,"dt":1737532800,"feels_like":276.32,"humidity":94,"pop":1,"pressure":1004,"rain":{"1h":0.3},"temp":276.32,"uvi":0,"visibility":10000,"weather":[{"description":"light rain","icon":"10d","id":500,"main":"Rain"}],"wind_deg":21,"wind_gust":2.75,"wind_speed":1.27},{"clouds":100,"dew_point":275.8,"dt":1737536400,"feels_like":275.16,"humidity":95,"pop":1,"pressure":1004,"rain":{"1h":0.17},"temp":276.52,"uvi":0.02,"visibility":10000,"weather":[{"description":"light rain","icon":"10d","id":500,"main":"Rain"}],"wind_deg":14,"wind_gust":3.34,"wind_speed":1.56},{"clouds":100,"dew_point":275.88,"dt":1737540000,"feels_like":275.72,"humidity":94,"pop":0.8,"pressure":1004,"temp":276.82,"uvi":0.05,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":351,"wind_gust":3.03,"wind_speed":1.4},{"clouds":100,"dew_point":275.73,"dt":1737543600,"feels_like":275.47,"humidity":93,"pop":0.8,"pressure":1004,"temp":276.89,"uvi":0.07,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":355,"wind_gust":3.93,"wind_speed":1.64},{"clouds":100,"dew_point":275.57,"dt":1737547200,"feels_like":275.6,"humidity":91,"pop":0.8,"pressure":1003,"temp":276.99,"uvi":0.08,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":349,"wind_gust":3.77,"wind_speed":1.63},{"clouds":100,"dew_point":275.47,"dt":1737550800,"feels_like":275.65,"humidity":90,"pop":0,"pressure":1003,"temp":277.01,"uvi":0.08,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":344,"wind_gust":3.52,"wind_speed":1.61},{"clouds":100,"dew_point":275.45,"dt":1737554400,"feels_like":275.33,"humidity":90,"pop":0,"pressure":1003,"temp":277,"uvi":0.08,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":328,"wind_gust":4.44,"wind_speed":1.86},{"clouds":100,"dew_point":275.39,"dt":1737558000,"feels_like":275.21,"humidity":89,"pop":0,"pressure":1002,"temp":277.15,"uvi":0.1,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":336,"wind_gust":5.81,"wind_speed":2.14},{"clouds":100,"dew_point":274.91,"dt":1737561600,"feels_like":275.62,"humidity":85,"pop":0,"pressure":1002,"temp":277.26,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":332,"wind_gust":5.28,"wind_speed":1.87},{"clouds":100,"dew_point":274.46,"dt":1737565200,"feels_like":275.13,"humidity":86,"pop":0,"pressure":1003,"temp":276.68,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":319,"wind_gust":4.44,"wind_speed":1.72},{"clouds":100,"dew_point":274.28,"dt":1737568800,"feels_like":274.89,"humidity":87,"pop":0,"pressure":1003,"temp":276.32,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":312,"wind_gust":4.45,"wind_speed":1.59},{"clouds":83,"dew_point":274.39,"dt":1737572400,"feels_like":274.38,"humidity":90,"pop":0,"pressure":1003,"temp":275.96,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":312,"wind_gust":4.75,"wind_speed":1.66},{"clouds":41,"dew_point":274.51,"dt":1737576000,"feels_like":273.92,"humidity":93,"pop":0,"pressure":1003,"temp":275.59,"uvi":0,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03n","id":802,"main":"Clouds"}],"wind_deg":303,"wind_gust":4.09,"wind_speed":1.69},{"clouds":30,"dew_point":274.64,"dt":1737579600,"feels_like":273.76,"humidity":95,"pop":0,"pressure":1004,"temp":275.4,"uvi":0,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03n","id":802,"main":"Clouds"}],"wind_deg":304,"wind_gust":3.28,"wind_speed":1.64},{"clouds":33,"dew_point":274.81,"dt":1737583200,"feels_like":274.21,"humidity":95,"pop":0,"pressure":1004,"temp":275.54,"uvi":0,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03n","id":802,"main":"Clouds"}],"wind_deg":285,"wind_gust":1.52,"wind_speed":1.44},{"clouds":37,"dew_point":274.87,"dt":1737586800,"feels_like":275.73,"humidity":95,"pop":0,"pressure":1004,"temp":275.73,"uvi":0,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03n","id":802,"main":"Clouds"}],"wind_deg":279,"wind_gust":1.02,"wind_speed":1.16},{"clouds":35,"dew_point":274.71,"dt":1737590400,"feels_like":274.35,"humidity":94,"pop":0,"pressure":1004,"temp":275.6,"uvi":0,"visibility":10000,"weather":[{"description":"scattered clouds","icon":"03n","id":802,"main":"Clouds"}],"wind_deg":288,"wind_gust":1.31,"wind_speed":1.39},{"clouds":7,"dew_point":274.59,"dt":1737594000,"feels_like":273.74,"humidity":95,"pop":0,"pressure":1004,"temp":275.38,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":257,"wind_gust":1.44,"wind_speed":1.64},{"clouds":7,"dew_point":274.12,"dt":1737597600,"feels_like":272.87,"humidity":93,"pop":0,"pressure":1005,"temp":275.19,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":241,"wind_gust":5.9,"wind_speed":2.18},{"clouds":7,"dew_point":273.08,"dt":1737601200,"feels_like":272.44,"humidity":88,"pop":0,"pressure":1005,"temp":274.87,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":232,"wind_gust":6.4,"wind_speed":2.23},{"clouds":7,"dew_point":272.55,"dt":1737604800,"feels_like":271.97,"humidity":86,"pop":0,"pressure":1005,"temp":274.66,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":228,"wind_gust":7.61,"wind_speed":2.45},{"clouds":7,"dew_point":272.87,"dt":1737608400,"feels_like":271.64,"humidity":88,"pop":0,"pressure":1005,"temp":274.76,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":229,"wind_gust":10.09,"wind_speed":2.93},{"clouds":10,"dew_point":273.52,"dt":1737612000,"feels_like":271.84,"humidity":92,"pop":0,"pressure":1005,"temp":274.72,"uvi":0,"visibility":10000,"weather":[{"description":"clear sky","icon":"01n","id":800,"main":"Clear"}],"wind_deg":215,"wind_gust":10.15,"wind_speed":2.65},{"clouds":98,"dew_point":273.75,"dt":1737615600,"feels_like":272.44,"humidity":91,"pop":0,"pressure":1005,"temp":275.17,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":208,"wind_gust":11,"wind_speed":2.59},{"clouds":52,"dew_point":274.02,"dt":1737619200,"feels_like":272.17,"humidity":94,"pop":0,"pressure":1005,"temp":274.9,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":190,"wind_gust":11.26,"wind_speed":2.53},{"clouds":63,"dew_point":275.08,"dt":1737622800,"feels_like":273.27,"humidity":92,"pop":0,"pressure":1005,"temp":276.31,"uvi":0.21,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04d","id":803,"main":"Clouds"}],"wind_deg":195,"wind_gust":13.99,"wind_speed":3.23},{"clouds":72,"dew_point":276.21,"dt":1737626400,"feels_like":275.17,"humidity":85,"pop":0.2,"pressure":1004,"rain":{"1h":0.11},"temp":278.67,"uvi":0.31,"visibility":10000,"weather":[{"description":"light rain","icon":"10d","id":500,"main":"Rain"}],"wind_deg":205,"wind_gust":12.2,"wind_speed":4.94},{"clouds":78,"dew_point":277.54,"dt":1737630000,"feels_like":275.7,"humidity":90,"pop":0.8,"pressure":1003,"rain":{"1h":0.64},"temp":279.14,"uvi":0.39,"visibility":10000,"weather":[{"description":"light rain","icon":"10d","id":500,"main":"Rain"}],"wind_deg":203,"wind_gust":12.46,"wind_speed":5.05},{"clouds":81,"dew_point":277.21,"dt":1737633600,"feels_like":276.74,"humidity":82,"pop":1,"pressure":1002,"rain":{"1h":0.3},"temp":280.21,"uvi":0.21,"visibility":10000,"weather":[{"description":"light rain","icon":"10d","id":500,"main":"Rain"}],"wind_deg":210,"wind_gust":14.46,"wind_speed":5.78},{"clouds":100,"dew_point":278.62,"dt":1737637200,"feels_like":276.28,"humidity":92,"pop":1,"pressure":999,"rain":{"1h":1.66},"temp":279.92,"uvi":0.06,"visibility":5961,"weather":[{"description":"moderate rain","icon":"10d","id":501,"main":"Rain"}],"wind_deg":204,"wind_gust":16.75,"wind_speed":6.04},{"clouds":100,"dew_point":278.36,"dt":1737640800,"feels_like":276.81,"humidity":85,"pop":1,"pressure":999,"rain":{"1h":1.34},"temp":280.84,"uvi":0.06,"visibility":10000,"weather":[{"description":"moderate rain","icon":"10d","id":501,"main":"Rain"}],"wind_deg":237,"wind_gust":16.27,"wind_speed":8.04},{"clouds":100,"dew_point":277.3,"dt":1737644400,"feels_like":277.04,"humidity":78,"pop":1,"pressure":999,"rain":{"1h":0.28},"temp":280.9,"uvi":0.16,"visibility":10000,"weather":[{"description":"light rain","icon":"10d","id":500,"main":"Rain"}],"wind_deg":257,"wind_gust":15.66,"wind_speed":7.52},{"clouds":98,"dew_point":276.1,"dt":1737648000,"feels_like":276.49,"humidity":74,"pop":0.8,"pressure":1000,"temp":280.44,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04d","id":804,"main":"Clouds"}],"wind_deg":252,"wind_gust":14.39,"wind_speed":7.35},{"clouds":81,"dew_point":275.8,"dt":1737651600,"feels_like":275.48,"humidity":77,"pop":0.8,"pressure":1002,"temp":279.59,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":256,"wind_gust":14.46,"wind_speed":7.11},{"clouds":82,"dew_point":276.26,"dt":1737655200,"feels_like":275.82,"humidity":81,"pop":0.8,"pressure":1003,"temp":279.38,"uvi":0,"visibility":10000,"weather":[{"description":"broken clouds","icon":"04n","id":803,"main":"Clouds"}],"wind_deg":255,"wind_gust":11.87,"wind_speed":5.48},{"clouds":95,"dew_point":275.75,"dt":1737658800,"feels_like":275.14,"humidity":81,"pop":0,"pressure":1004,"temp":278.89,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":251,"wind_gust":12.73,"wind_speed":5.61},{"clouds":100,"dew_point":275.44,"dt":1737662400,"feels_like":274.94,"humidity":80,"pop":0,"pressure":1004,"temp":278.61,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":247,"wind_gust":11.93,"wind_speed":5.27},{"clouds":90,"dew_point":275.29,"dt":1737666000,"feels_like":275.13,"humidity":83,"pop":0,"pressure":1004,"temp":278.07,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":226,"wind_gust":9.62,"wind_speed":3.63},{"clouds":92,"dew_point":274.9,"dt":1737669600,"feels_like":274.82,"humidity":80,"pop":0,"pressure":1005,"temp":278.19,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":218,"wind_gust":12.1,"wind_speed":4.44},{"clouds":94,"dew_point":274.77,"dt":1737673200,"feels_like":275.21,"humidity":77,"pop":0,"pressure":1004,"temp":278.45,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":206,"wind_gust":13.08,"wind_speed":4.3},{"clouds":95,"dew_point":275.24,"dt":1737676800,"feels_like":275.7,"humidity":78,"pop":0,"pressure":1003,"temp":278.83,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":193,"wind_gust":13.68,"wind_speed":4.27},{"clouds":100,"dew_point":277.72,"dt":1737680400,"feels_like":276.38,"humidity":86,"pop":0,"pressure":1001,"temp":279.96,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":194,"wind_gust":14.65,"wind_speed":5.89},{"clouds":100,"dew_point":278.52,"dt":1737684000,"feels_like":276.76,"humidity":87,"pop":0,"pressure":999,"temp":280.58,"uvi":0,"visibility":10000,"weather":[{"description":"overcast clouds","icon":"04n","id":804,"main":"Clouds"}],"wind_deg":182,"wind_gust":18.79,"wind_speed":7.07},{"clouds":100,"dew_point":279.97,"dt":1737687600,"feels_like":277.54,"humidity":91,"pop":0.34,"pressure":997,"rain":{"1h":0.15},"temp":281.56,"uvi":0,"visibility":10000,"weather":[{"description":"light rain","icon":"10n","id":500,"main":"Rain"}],"wind_deg":192,"wind_gust":20.34,"wind_speed":8.81},{"clouds":100,"dew_point":280.36,"dt":1737691200,"feels_like":278.31,"humidity":88,"pop":1,"pressure":995,"rain":{"1h":0.73},"temp":282.35,"uvi":0,"visibility":10000,"weather":[{"description":"light rain","icon":"10n","id":500,"main":"Rain"}],"wind_deg":194,"wind_gust":21.96,"wind_speed":9.95}],"lat":51.5085,"lon":-0.1257,"minutely":[{"dt":1737523440,"precipitation":0},{"dt":1737523500,"precipitation":0},{"dt":1737523560,"precipitation":0},{"dt":1737523620,"precipitation":0},{"dt":1737523680,"precipitation":0},{"dt":1737523740,"precipitation":0},{"dt":1737523800,"precipitation":0},{"dt":1737523860,"precipitation":0},{"dt":1737523920,"precipitation":0},{"dt":1737523980,"precipitation":0},{"dt":1737524040,"precipitation":0},{"dt":1737524100,"precipitation":0},{"dt":1737524160,"precipitation":0},{"dt":1737524220,"precipitation":0},{"dt":1737524280,"precipitation":0},{"dt":1737524340,"precipitation":0},{"dt":1737524400,"precipitation":0},{"dt":1737524460,"precipitation":0},{"dt":1737524520,"precipitation":0},{"dt":1737524580,"precipitation":0},{"dt":1737524640,"precipitation":0},{"dt":1737524700,"precipitation":0},{"dt":1737524760,"precipitation":0},{"dt":1737524820,"precipitation":0},{"dt":1737524880,"precipitation":0},{"dt":1737524940,"precipitation":0},{"dt":1737525000,"precipitation":0},{"dt":1737525060,"precipitation":0},{"dt":1737525120,"precipitation":0},{"dt":1737525180,"precipitation":0},{"dt":1737525240,"precipitation":0},{"dt":1737525300,"precipitation":0},{"dt":1737525360,"precipitation":0},{"dt":1737525420,"precipitation":0},{"dt":1737525480,"precipitation":0},{"dt":1737525540,"precipitation":0},{"dt":1737525600,"precipitation":0},{"dt":1737525660,"precipitation":0},{"dt":1737525720,"precipitation":0},{"dt":1737525780,"precipitation":0},{"dt":1737525840,"precipitation":0},{"dt":1737525900,"precipitation":0},{"dt":1737525960,"precipitation":0},{"dt":1737526020,"precipitation":0},{"dt":1737526080,"precipitation":0},{"dt":1737526140,"precipitation":0},{"dt":1737526200,"precipitation":0},{"dt":1737526260,"precipitation":0},{"dt":1737526320,"precipitation":0},{"dt":1737526380,"precipitation":0},{"dt":1737526440,"precipitation":0},{"dt":1737526500,"precipitation":0},{"dt":1737526560,"precipitation":0},{"dt":1737526620,"precipitation":0},{"dt":1737526680,"precipitation":0},{"dt":1737526740,"precipitation":0},{"dt":1737526800,"precipitation":0},{"dt":1737526860,"precipitation":0},{"dt":1737526920,"precipitation":0},{"dt":1737526980,"precipitation":0}],"timezone":"Europe/London","timezone_offset":0}



    # Comment below for offline mode
    # # Get basic info about the city
    # geo = getLatLongByCity("tampa")

    # # Get weather data
    # data = getDataWLatLong(geo['lat'], geo['long'])


    forecast = {}

    # Get the forecast from the json
    for num, i in enumerate(data['daily']):
        forecast[num] = {
            "day": epoch_to_day_of_week(i['dt']),
            "datetime": epoch_to_datetime(i['dt']),
            "temp": kelvin_to_fahrenheit( i['temp']['day'] ),
            "feels_like": kelvin_to_fahrenheit( i['feels_like']['day'] ),
            "max_temp": kelvin_to_fahrenheit( i['temp']['max'] ),
            "min_temp": kelvin_to_fahrenheit( i['temp']['min'] ),
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
        "temp": kelvin_to_fahrenheit(data['current']['temp']),
        "feels_like": kelvin_to_fahrenheit(data['current']['feels_like']),
        "humidity": data['current']['humidity'],
        "uvi": data['current']["uvi"],
        "wind_direction": data['current']['wind_deg'],
        "wind_speed": data['current']['wind_speed'],
    }

    
    context = {}

    context['now'] = now
    context['forecast'] = forecast
    context['geo'] = geo
    
    return context
    # return forecast
    # return data