import requests, json 
import streamlit as st
from datetime import date

st.title("Good Morning!")
current_date = date.today()
st.markdown("Today is "+str(current_date)+", "+current_date.strftime('%A'))
st.markdown("## Weather")

api_key = "ac78d812f2287fd1958216aff7f1957d"
base_url = "http://api.openweathermap.org/data/2.5/group?"

city_dict = {"San Francisco":"5391997", "Foster City":"5350159"}
ids = ','.join(city_dict.values())
complete_url = base_url + "appid=" + api_key + "&id=" + ids + "&units=metric"

@st.cache
def fetch_api(url):
    response = requests.get(url) 
    x = response.json()
    return x 

city_weather = fetch_api(complete_url)
for x in city_weather['list']:
    y = x["main"] 
    current_temperature = y["temp"] 
    max_temperature = y["temp_max"] 
    min_temperature = y["temp_min"] 
    z = x["weather"]
    weather_description = z[0]["description"]
    city = x['name']
    st.markdown(city + " has " + str(weather_description))
    st.markdown("Currently at " + str(current_temperature) + "&deg;C")
    st.markdown("With highest at " + str(max_temperature) + "&deg;C")
    st.markdown("and lowest at " + str(min_temperature) + "&deg;C")