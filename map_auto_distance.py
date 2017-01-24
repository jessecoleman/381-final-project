from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re


with open('buildings.txt', 'r') as file:
	buildings = file.readlines()
	buildings = [b.split(' ')[0] for b in buildings]
	i = 0
	error = 0
	
	with open('distances.txt', 'w') as out:
		# write header
		out.write(',' + re.split('\[|\]', str(buildings))[1] + '\n')
		print(',' + re.split('\[|\]', str(buildings))[1] + '\n')	
	for b in buildings:
		i = i + 1
		if i > 27:	
			with open('distances.txt', 'w') as out:
				browser = webdriver.Chrome()
				browser.get('https://www.washington.edu/maps/')
				browser.implicitly_wait(10)
	
				script =                "$(function(){" + \
       	         			        	"$.fx.off = true;" + \
       	                		         		"var styleEl = document.createElement('style');" + \
       	                        			"styleEl.textContent = '*{ transition: none !important; transition-property: none !important; }';" + \
       	                        			"document.head.appendChild(styleEl);" + \
       	                     			"});" 
				browser.execute_script(script)
	
				directions = browser.find_element_by_id('switcher-directions')
				directions.click()
	
				search_current = browser.find_element_by_id('current')
				search_destination = browser.find_element_by_id('destination')
	
				prev_details = ''
				row = b + ','
				j = 0
				for b2 in buildings:
					j = j + 1
					if i < j and b != b2:
						search_current.clear()
						search_current.send_keys(b + Keys.RETURN)
						result = browser.find_element(By.CLASS_NAME, 'search-result')
						result.click()
						search_destination.clear()
						search_destination.send_keys(b2 + Keys.RETURN)
						result = browser.find_element(By.CLASS_NAME, 'search-result')
						result.click()
						time.sleep(0.8)
						details = browser.find_element(By.CLASS_NAME, 'print').text	
						if details == prev_details:
							time.sleep(1.6)
							search_current.clear()
							search_current.send_keys(b + Keys.RETURN)
							result = browser.find_element(By.CLASS_NAME, 'search-result')
							result.click()
							search_destination.clear()
							search_destination.send_keys(b2 + Keys.RETURN)
							result = browser.find_element(By.CLASS_NAME, 'search-result')
							result.click()
							time.sleep(0.8)
							details = browser.find_element(By.CLASS_NAME, 'print').text
						if details == prev_details:
							error = error + 1
						prev_details = details
						output = details.split(' ')
						try:
							output = output[0] + ' ' +  output[4]
						except:
							output = 'error'
						row = row + output + ','
					else:
						row = row + ","
					search_current.clear()
				out.write(row[:-1] + '\n')
				print(row[:-1] + '\n')
				browser.close()
print('error' + error)
