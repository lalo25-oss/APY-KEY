# -*- coding: utf-8 -*-
"""
@author: jose alfredo jimenez elizondo
"""
#se importan todos los modulos necesario 
import requests
import urllib
import webbrowser

# se realiza una petición a la API de Google Maps Directions entre dos localidades y se proceza el JSON
api = "https://maps.googleapis.com/maps/api/directions/json?"
apik= "&mode=driving&Language=es&Units=Metric&key=AQUIVALAAPIKEY"

L1= raw_input ("ingrese el lugar de origen: ")
L2= raw_input ("ingrese el lugar de destino: ")

url= api + urllib.urlencode({"origin":L1,"destination":L2}) + apik
print "\nurl de la Api key: ", url

json_data=requests.get(url).json()
print (json_data)

# se muestra en un mapa la ruta.
ma= "https://www.google.com/maps/dir/?api=1&"
mode= "&travelmode=driving"
mapa= ma + urllib.urlencode({"origin":L1,"destination":L2}) + mode
mapau= "mapa"
print "\nurl de la ruta en google maps: ", mapa 

webbrowser.open_new_tab(mapa)
