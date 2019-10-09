import requests, json 
import streamlit as st

st.title("Daily Commute")
st.markdown("## Weather")

api_key = "ac78d812f2287fd1958216aff7f1957d"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
id = "5391997"
city_name = "San Francisco"
complete_url = base_url + "appid=" + api_key + "&id=" + id + "&units=metric"

@st.cache
def fetch_api(url):
    response = requests.get(url) 
    x = response.json()
    return x 

x = fetch_api(complete_url)
if x["cod"] == "404": 
    " City Not Found "
elif x["cod"] == "429": 
    " Account is temporary blocked "
else: 
    y = x["main"] 
    current_temperature = y["temp"] 
    max_temperature = y["temp_max"] 
    min_temperature = y["temp_min"] 
    z = x["weather"]
    weather_description = z[0]["description"]
    st.markdown("San Francisco has " + str(weather_description))
    st.markdown("Current temperature is " + str(current_temperature))
    st.markdown("Highest temperature is " + str(max_temperature))
    st.markdown("Lowest temperature is " + str(min_temperature))