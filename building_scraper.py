from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re

url = "https://www.washington.edu/students/reg/buildings.html"
site = bs(urlopen(url).read(), "html.parser")

codes = site.find('div', {'class', 'container uw-body'}).findAll('code')

for c in codes:
	try: 
		building = site.find(href='/maps/?l=' + c.text.lower())
		#print('/maps/?l=' + c.text.lower())
		print(c.text + " " + building.text)
	except:
		print(c.text + ' error')


