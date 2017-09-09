# -*- coding: utf-8 -*- 

from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys 

from bs4 import BeautifulSoup
from datetime import *
import time 
import os 
import urllib, urllib2
import codecs

code = "2330"
year = 97	
end = 96
doc = "http://http://doc.twse.com.tw"


browser = webdriver.Chrome('chromedriver') 
browser.window_handles
browser.implicitly_wait(20)
windowscount = 0;

while(year != end):
	#url = "http://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id="+code+"&year="+str(year)+"&seamon=&mtype=A&"
	url = "http://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id="+code+"&year="+str(year)+"&seamon=&mtype=F&"
	browser.get(url)
	items = browser.find_elements_by_xpath('//a')
	i = 1
	for item in items:
		i += 1
		eng = browser.find_element_by_xpath('//html/body/center/form/table[2]/tbody/tr['+str(i)+']/td[6]').text
		print eng
		if u"英文" in eng:
			continue
		if u"年報" not in eng:
			continue
		if u"關係表" in eng:
			continue
		item.click()#get_attribute("href").onclick()
		time.sleep(2)
		windowscount += 1
		try:
			browser.switch_to_window(browser.window_handles[1])
		except:
			continue
		link = browser.find_element_by_xpath('//a')
		print link.get_attribute("href")
		print link.text
		testfile = urllib.URLopener()
		testfile.retrieve(link.get_attribute("href"), link.text)
		browser.close()
		browser.switch_to_window(browser.window_handles[0])
		time.sleep(2)
	time.sleep(3)


	year -=1

browser.close()