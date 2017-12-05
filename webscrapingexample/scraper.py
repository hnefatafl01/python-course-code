import requests
from bs4 import BeautifulSoup

req=requests.get('http://pythonhow.com/example.html')
contents=req.content
# print(content)
soup=BeautifulSoup(contents,'html.parser')
all=soup.find_all('div', {'class':'cities'})
# print(all)
for item in all:
    print(item.find_all('h2')[0].text)
