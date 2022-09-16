from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

numbers = []
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) > 1:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
else:
    html = urlopen("https://py4e-data.dr-chuck.net/comments_1620118.html", context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    

span_tags = soup("span")

for tag in list(span_tags):
    tag = str(tag)
    lst = re.findall("[0-9]+", tag)
    numbers.append(int(lst[0])) 
print(sum(numbers))

