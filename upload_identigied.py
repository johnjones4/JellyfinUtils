import requests
import os
import csv

JELLYFIN_API_KEY = os.environ['JELLYFIN_API_KEY']
JELLYFIN_HOST = os.environ['JELLYFIN_HOST']
JELLYFIN_USER_ID = os.environ['JELLYFIN_USER_ID']
JELLYFIN_MOVIES_FOLDER_ID = os.environ['JELLYFIN_MOVIES_FOLDER_ID']

USER_ID_PARAMS = {'userId': JELLYFIN_USER_ID}
AUTH_HEADERS = {
    'Authorization': f"MediaBrowser Token={JELLYFIN_API_KEY}",
    'Content-type': 'application/json'
}

RAW_ITEM = {
  "AirDays": [],
  "AirsAfterSeasonNumber": "",
  "AirsBeforeEpisodeNumber": "",
  "AirsBeforeSeasonNumber": "",
  "AirTime": "",
  "Album": "",
  "AlbumArtists": [],
  "ArtistItems": [],
  "AspectRatio": "",
  "CommunityRating": "8",
  "CriticRating": "",
  "CustomRating": "",
  "DateCreated": "",
  "DisplayOrder": "",
  "EndDate": None,
  "ForcedSortName": "",
  "Genres": [],
  "Height": "",
  "Id": "",
  "IndexNumber": None,
  "LockData": False,
  "LockedFields": [],
  "Name": "",
  "OfficialRating": "",
  "OriginalTitle": "",
  "Overview": "",
  "ParentIndexNumber": None,
  "People": [],
  "PreferredMetadataCountryCode": "",
  "PreferredMetadataLanguage": "",
  "PremiereDate": "",
  "ProductionYear": "",
  "ProviderIds": {},
  "Status": "",
  "Studios": [],
  "Taglines": [],
  "Tags": [],
  "Video3DFormat": ""
}

with open("./identified.csv", "r") as file:
    csvreader = csv.DictReader(file, fieldnames=['name', 'id', 'tmdb', 'tmdbCollection', 'imdb'])
    for row in csvreader:
        item = requests.get(JELLYFIN_HOST + '/Items/', params={"ids": [row['id']]}, headers=AUTH_HEADERS).json()['Items'][0]
        item = RAW_ITEM | item
        item['Name'] = row['name']
        item['ProviderIds'] = {}
        if row['tmdb']:
            item['ProviderIds']['Tmdb'] = row['tmdb']
        if row['tmdbCollection']:
            item['ProviderIds']['TmdbCollection'] = row['tmdbCollection']
        if row['imdb']:
            item['ProviderIds']['Imdb'] = row['imdb']
        print(f"Updating {row['name']}")
        res = requests.post(JELLYFIN_HOST + '/Items/' + row['id'], json=item, headers=AUTH_HEADERS)
        print(res)

        print(f"Refreshing {row['name']}")
        res = requests.post(JELLYFIN_HOST + '/Items/' + row['id'] + '/Refresh', params={"metadataRefreshMode": "FullRefresh", "imageRefreshMode": "FullRefresh", "replaceAllMetadata": True, "replaceAllImages": True}, headers=AUTH_HEADERS)
        print(res)

    