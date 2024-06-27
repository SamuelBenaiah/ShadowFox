from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_Indian_male_film_actors'

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")
print(soup)