from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
# -*- coding: utf-8 -*-

def get_classes(url):
	subsite = ''
	try:
		subsite = bs(urlopen(url), "html.parser")
	except:
		print('error')
		return
	
	print(subsite.title)
	courses = subsite.find_all('pre')
	#print(classes)
	for c in courses:
		out = str(c).split()
		for o in out:
			try:
				print(o)
			except:
				print('error')


url = "https://www.washington.edu/students/reg/buildings.html"
site = bs(urlopen(url).read(), "html.parser")

codes = site.find('div', {'class', 'container uw-body'}).findAll('code')

#for c in codes:
	#try: 
		#building = site.find(href='/maps/?l=' + c.text.lower())
		#print('/maps/?l=' + c.text.lower())
		#print(c.text + " " + building.text)
	#except:
		#print(c.text + ' error')

url = "https://www.washington.edu/students/timeschd/WIN2017/"
site = bs(urlopen(url).read(), "html.parser")

links = site.findAll('a')#.next_sibling().findAll('li')
#print(links)

pos = 0
for link in links:
	link = str(link).split('\"')[1]
	if '/' not in link and 'html' in link:
		get_classes(url + link)
	pos = pos + 1


