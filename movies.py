from bs4 import BeautifulSoup
from requests import get
import pandas as pd
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
genres =[]
votes = []
# Extract data from individual movie container
for container in movie_containers:
# If the movie has Metascore, then extract:
    if container.find('div', class_ = 'ratings-metascore') is not None:
# The name
        name = container.h3.a.text
        names.append(name)
# The year
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)
# The IMDB rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
# The Metascore

#genre
        genre=container.p.find('span', class_='runtime').text
        genres.append(genre)

        m_score = container.find('span', class_ = 'metascore').text
        metascores.append(int(m_score))
# The number of votes
        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))

df = pd.DataFrame(data={"Name": names, "Year": years, "Genres":genres})
df.to_csv("./file.csv", sep=',',index=False)

print(genres)
