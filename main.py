from fastapi import FastAPI
from decouple import config
import requests
from functools import partial
from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent='dwp')
geocode  = partial(geolocator.geocode, language='es')
url = config('URL')
url_path  = '{url}/users'.format(url=url)
app = FastAPI()

@app.get("/")
def root():
    return {"Hello":"Welcome to DWP API test"}


@app.get("/people")
async def get_people():

    try:
        resp = requests.get(url_path)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'code':'404'}
    except:
        return {'code':'400'}


@app.get("/people/city/")
async def get_people_in_city(city:str='london',miles:int=50):

    location = geocode(city.lower())
    city_lat_long  = (float('{:.6f}'.format(location.latitude)),float('{:.7f}'.format(location.longitude)))
    try:
        resp  = requests.get(url_path)
        if resp.status_code == 200:
            people = []
            result = resp.json()
            for index in result:
                city_distance = float('{:1f}'.format(distance.distance((city_lat_long),(float(index['latitude']),float(index['longitude']))).miles))
                if city_distance <= float(miles):
                    people.append(index)
            return people
        else:
            return {'code':'404'}
    except:
        return {'code':'400'}