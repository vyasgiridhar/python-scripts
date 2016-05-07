#!/usr/bin/env python2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

def main() :

	authurl = "https://firewall.amritanet.edu:8443/auth1.html"
	delay = 3
	print "\n\n[*]  Opening a New Session.."
	driver = webdriver.Firefox()
	driver.get(authurl)

	assert "Sonic" in driver.title

	print "\n\n[*] Enumerating Login Page.."
	user = driver.find_element_by_name("userName")
	passwd = driver.find_element_by_name("pwd")

	print "\n\n[*] Sending Credentials .. "
	user.send_keys("cse14002")
	passwd.send_keys("goodstash")
	passwd.send_keys(Keys.RETURN)

	print "\n\n[*] Login Done!"
	driver.quit()
def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

while True:
	if internet_on():	
		main()
