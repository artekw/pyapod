#!/usr/bin/python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urlparse import urlsplit
from urllib2 import urlopen, HTTPError, URLError
import os

root = "http://apod.nasa.gov/apod"

print "Astronomy Picture of the Day by NASA"
print "Wait..."

page = urlopen(root)
soup = BeautifulSoup(page)
imgsrc = soup.findAll('img')
url = "%s/%s" % (root, imgsrc[0]['src'])
try:
	f = urlopen(url).read()
	fName = os.path.basename(urlsplit(url)[2])
	print "Downloading " + url

	output = open(fName,'wb')
	output.write(f)
	output.close()
	print "Renaming to apod.jpg"
	os.rename(fName, "apod.jpg")
	print "Done!"

except HTTPError, e:
	print "HTTP Error:", e.code, url
except URLError, e:
	print "URL Error:", e.reason, url
