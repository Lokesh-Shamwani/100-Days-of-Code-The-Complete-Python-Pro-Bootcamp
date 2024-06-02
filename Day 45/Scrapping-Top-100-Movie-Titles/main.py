import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")
movies_elements = soup.find_all("h3", class_="title")
movies_names = [element.text for element in movies_elements]

with open("./movies.txt", "w" ,encoding='utf-8') as file:
    for i in range( (len(movies_names)-1), -1, -1):
        file.write(movies_names[i]+ "\n")
    