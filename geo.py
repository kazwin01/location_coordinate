from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import pandas as pd 
import numpy as np

file = input("Enter the full path to the data file:\n")
countries =  pd.read_csv(str(file), usecols=[0])
df =  pd.DataFrame(countries)
longitude = []
latitude = []
   
def findGeocode(country):
       
    try:
        geolocator = Nominatim(user_agent="amirukz1@gmail.com")
        return geolocator.geocode(country)
      
    except GeocoderTimedOut:  
        return findGeocode(country)    
  
for i in (df["country"]):
      
    if findGeocode(i) != None:
           
        loc = findGeocode(i)
        latitude.append(loc.latitude)
        longitude.append(loc.longitude)
       
    else:
        latitude.append(np.nan)
        longitude.append(np.nan)
    print (i + ' OK')
df["Longitude"] = longitude
df["Latitude"] = latitude

print(df)
df.to_csv('coordinate.csv', sep = ',', index = False)
