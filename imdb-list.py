from bs4 import BeautifulSoup
import requests
import re

url = 'endereço-da-lista-IMDb'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('h3.lister-item-header')
links = [a.attrs.get('href') for a in soup.select('h3.lister-item-header  a')]
crew = [a.attrs.get('title') for a in soup.select('h3.lister-item-header  a')]


imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    data = {"movie_title": movie_title,
            "year": year
           }
    imdb.append(data)

print('Nome'+',','Ano')
for item in imdb:
    print(item['movie_title']+',', item['year'])