import urllib.request as ur
from bs4 import BeautifulSoup as bs
ba="https://github.com"
rl=bs(ur.urlopen(ba+"/trending/python"),'lxml').find_all("h1",{"class":"h3 lh-condensed"})
[print(f'{i+1:02}: {ba}{rl[i].find("a").get("href")}')for i in range(10)]
