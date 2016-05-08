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
	driver.wait(10)
	print "\n\n[*] Login Done!"
	driver.quit()
def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return False
    except urllib2.URLError as err: pass
    return True
'''
while True:
	if internet_on():	
		main()
'''
main()
