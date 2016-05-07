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
	passwd.send_keys("plplplplpl")
	passwd.send_keys(Keys.RETURN)

	driver.get("http://www.msftncsi.com/ncsi.txt")

	print "\n\n[*] Login Done!"
	driver.quit()


main()
