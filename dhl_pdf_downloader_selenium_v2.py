from splinter import Browser
import os
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#browser = Browser()

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.dir", "/home/dhl/download")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

webdriver = webdriver.Firefox(firefox_profile=fp)

webdriver.get('https://nolb.dhl.de/nextt-online-business/jsp/login.do')

#Loging in
webdriver.find_element_by_id('login').send_keys('user')
webdriver.find_element_by_id('password').send_keys('password')
webdriver.find_element_by_name('doLogin').click()

f = open("/home/dhl/shipment_numbers.csv")

wait = WebDriverWait(webdriver, 60 * 60)

for line in f:
	#Searching for shipment code
	webdriver.find_element_by_id('shipmentCode').send_keys(line)
	webdriver.find_element_by_id('timeIntervall').send_keys('12')
	webdriver.find_element_by_name('search_ta').click()
	#Downloading pdf
	try:
	    actionSelection = wait.until(EC.element_to_be_clickable((By.ID,'pageActionSelect')))
	finally:
		pass
	actionSelection.send_keys('download')
	webdriver.execute_script('javascript:openLayerSelection(\'pieceList\',\'false\')')
	#webdriver.find_element_by_id('signchk').click()
	try:
	    element = wait.until(EC.element_to_be_clickable((By.ID,'signchk')))
	finally:
		pass
	element.click()
	webdriver.find_element_by_xpath("//input[@value='Download']").click()

	webdriver.implicitly_wait(600)
	webdriver.find_element_by_name('cancel_ta').click()
	print "downloaded shipment pdf with shipment code :" + line
   
f.close()
