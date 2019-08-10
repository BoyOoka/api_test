from bs4 import BeautifulSoup
import requests
import re
import lxml

url = "http://www.cntour.cn"
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, "lxml")
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
print(type(data[0]))
result = []
for i in data:
    item = {
        "title": i.get_text(),
        "link": i.get('href'),
        "ID": re.findall('\\d+', i.get('href'))[0]
    }
    result.append(item)
print(result)
