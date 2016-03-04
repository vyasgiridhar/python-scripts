from bs4 import BeautifulSoup
import urllib2
import os

def ensure_dir(x):
    if not os.path.exists(x):
        os.mkdir(x)

def chive_from(x):
	soup = BeautifulSoup(urllib2.urlopen(x).read())
	try:
		Title = soup.find("header", { "class" : "article-header clearfix" }).find('h1').text
		ensure_dir(Title)
		os.chdir(Title)
		links = soup.findAll("div",{"class":"gallery-icon"})
		src = []
		for link in links:
			src.append(link.img.get('src'))
		import urllib	
		x = 0
		for l in src:
			print str(x)
			urllib.urlretrieve(l, str(x)+".jpg")
			x = x + 1
		os.chdir('..')
	except:
		os.chdir('..')
		return
		

return_soup = BeautifulSoup(urllib2.urlopen('http://thechive.com/category/girls/bikinis-girls/').read())
articles = main_soup.findAll("article")
for article in articles:
	print article.find('a').get('href')
	chive_from(article.find('a').get('href'))


