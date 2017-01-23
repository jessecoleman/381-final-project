import googlemaps
from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

gmaps = googlemaps.Client(key='AIzaSyA9icX7WfmrB-Lq4ncPCvMM8GEV9ft9F_Q')

url = 'https://www.washington.edu/maps/'

locations = bs(urlopen(url).read(), "html.parser")


with open('results.txt', 'r') as results:
	for line in results:
		print(line)
		building = gmaps.geocode(line + " UW, Washington")
		print(building)
