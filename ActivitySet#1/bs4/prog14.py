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
    x=tag.contents[0]
    sum+=int(tag)
print(tag)