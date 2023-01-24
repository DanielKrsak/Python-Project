from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movie_web_page = response.text
soup = BeautifulSoup(movie_web_page, "html.parser")

list_of_movies = [item.text for item in soup.find_all("h3", class_="title")]
list_of_movies.reverse()

with open("movies.txt", "w") as file:
    for item in list_of_movies:
        file.write(item)
        file.write("\n")

