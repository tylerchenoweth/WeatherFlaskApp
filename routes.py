from app import app

import random, requests, json, pandas as pd, numpy as np 


@app.route('/')
def index():
    
    API_Key = ""
    lat =
    long = 

    url = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"


