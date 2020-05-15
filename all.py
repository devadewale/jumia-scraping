from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import random as rnd
import time

pages = 0
brands = []
names = []
images=[]
links=[]
prices = []
while (pages < 50):

	useragent=["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3",

		   "AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0", 
		   "Safari/531.2+Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0",

		   "Safari/533.16 Mozilla/5.0 (Windows; U; Windows NT 6.1; es-ES) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0",

		   "AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2 Mozilla/5.0 (X11; Linux i686)",

		   "AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1 Mozilla/5.0 (X11; CrOS i686 0.13.587)",
		   "AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 DebianMozilla/5.0 (Windows; U; Windows NT 6.1; en-US)",
		   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36",
		   "AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0M ozilla/5.0 (Windows; U; Windows NT 5.2; en-US)",
		   "AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3 Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US)",
		   "AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3 Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US)",
		   "AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3 Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US)",
		   "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K)", 
		   "AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K)", 
		   "AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mozilla/5.0 (Linux; U; Android 2.3; en-us)",
		   "AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9 Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40)", 
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 MobileMozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40)", 
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91)", 
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D)",
		   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83)"]
	
	ag=rnd.randint(0,30)
	headers={'User-Agent':useragent[ag]}
	pages=pages+1
	URL = requests.get('https://www.jumia.com.ng/computing/?page='+str(pages),headers=headers)
	page_html = BeautifulSoup(URL.text, 'html.parser')
	items= page_html.find_all('div', class_ = 'sku -gallery')
	for item in items:
		brand=item.a.h2.find('span',class_='brand').text.strip()
		brands.append(brand)
		link=item.find('a')
		links.append(link.attrs['href'])
		name=item.a.h2.find('span', class_='name').text.strip()
		names.append(name)
		price=item.a.find('span', class_='price').text
		prices.append(price)
	time.sleep(3)
#print json format
#jsoni=[{ "brand":b, "name":n,"price":p}for b,n,p in zip(brands,names,prices)]
#print (json.dumps(jsoni))
#print(links)
#print(brands)
#print(names)
#print(prices)
df = pd.DataFrame(data={"Brand": brands, "Names": names, "Prices":prices, "Url":links})
df.to_csv("./juminacomputing.csv", sep=',',index=False)
