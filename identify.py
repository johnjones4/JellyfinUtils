import requests
import os
import csv

TMDB_API_KEY = os.environ['TMDB_API_KEY']
AUTH_HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer " + TMDB_API_KEY
}

found = list()

with open("./unidentified.csv", "r") as file2:
    csvfile = csv.reader(file2)
    for row in csvfile:
        id = row[0]
        name = row[1]
        results = requests.get("https://api.themoviedb.org/3/search/movie", params={"query": name, "language": "en-US", "include_adult": "false", "page": "1"}, headers=AUTH_HEADERS).json()['results']
        if results:
            found.append({
                'name': results[0]['title'],
                'id': id,
                'tmdb': results[0]['id']
            })

enriched = list()
for item in found:
    movie = requests.get("https://api.themoviedb.org/3/movie/" + str(item['tmdb']), params={"language": "en-US"}, headers=AUTH_HEADERS).json()
    if movie['belongs_to_collection']:
        item['tmdbCollection'] = movie['belongs_to_collection']['id']
    if movie['imdb_id']:
        item['imdb'] = movie['imdb_id']
    enriched.append(item)

with open("./identified.csv", "w") as file1:
    csvwriter = csv.DictWriter(file1, fieldnames=['name', 'id', 'tmdb', 'tmdbCollection', 'imdb'])
    for item in enriched:
        csvwriter.writerow(item)