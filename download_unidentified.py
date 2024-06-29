import requests
import os
import csv

JELLYFIN_API_KEY = os.environ['JELLYFIN_API_KEY']
JELLYFIN_HOST = os.environ['JELLYFIN_HOST']
JELLYFIN_USER_ID = os.environ['JELLYFIN_USER_ID']
JELLYFIN_MOVIES_FOLDER_ID = os.environ['JELLYFIN_MOVIES_FOLDER_ID']

USER_ID_PARAMS = {'userId': JELLYFIN_USER_ID}
AUTH_HEADERS = {
    'Authorization': f"MediaBrowser Token={JELLYFIN_API_KEY}"
}

with open("./unidentified.csv", "w") as file:
    writer = csv.writer(file)
    items = requests.get(JELLYFIN_HOST + '/Items', params=USER_ID_PARAMS | {'parentId':JELLYFIN_MOVIES_FOLDER_ID, 'limit': 100000, 'fields': ['ProviderIds']}, headers=AUTH_HEADERS).json()['Items']
    for item in items:
        print(item)
        if not item['ProviderIds']:
            writer.writerow([
                item['Id'],
                item['Name'].replace("_", " ").title(),
            ])