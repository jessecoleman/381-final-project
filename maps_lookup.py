import googlemaps
from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

gmaps = googlemaps.Client(key='AIzaSyA9icX7WfmrB-Lq4ncPCvMM8GEV9ft9F_Q')

url = 'https://www.washington.edu/maps/'

locations = bs(urlopen(url).read(), "html.parser")

def formatBuilding(b):
	building = ""
	l = b.split()
	flag = False
	for i in l:
		if flag:
			print(i)
			building = building + " " + i
		else:
			flag = True
	building = building + " (" + l[0] + ")"
	return building.split()
		

with open('buildings.txt', 'r') as results:
	r = results.readlines()

	for line in r:
		b1 = formatBuilding(line)
		for line2 in r:
			b2 = formatBuilding(line2)
			if b1 != b2:
				building = gmaps.geocode(b1)
				print(building)
