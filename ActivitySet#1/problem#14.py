 # Using Web Services
#https://www.py4e.com/lessons/servces
# import urllib.request, urllib.parse, urllib.error
# fhand=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1544659.html')
# for line in fhand:
#     words=line.decode().strip()
#     sum=sum(int(words))
# print(sum) 
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1544659.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
sum=0

tags = soup('span')
for tag in tags:
  
    sum =sum+tag
print(sum)