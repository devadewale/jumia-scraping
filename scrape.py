from bs4 import BeautifulSoup
import requests

URL = 'https://www.jumia.com.ng/computing/?page=1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
job_elems = soup.find_all('div', class_='sku -gallery')
for job_elem in job_elems:
     Brand = job_elem.find('span', class_='brand')
     Name = job_elem.find('span', class_='name')
     Price = job_elem.find('span', class_='price')
     # Rating = job_elem.find('div', class_='total-ratings')
     print(Brand.text.strip())
     print(Name.text.strip())
     print(Price.text.strip())
     # print(Ratings)
     print()
