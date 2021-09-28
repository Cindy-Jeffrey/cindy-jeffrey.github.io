import requests
import json
import urllib.request
from bs4 import BeautifulSoup as bs
import os
import re

# open index.html and parse
html = open('index.html')
soup = bs(html, 'html.parser')

# download the latest 6 videos and thumbnails from YouTube
url = 'https://www.googleapis.com/youtube/v3/search'
params = dict(
    key=os.environ.get('YOUTUBE_API_KEY'),
    channelId='UCEcFg4Zlzsw5tVoynPzXHnQ',
    part='snippet,id',
    order='date',
    maxResults=6
)
resp = requests.get(url=url, params=params)
data = resp.json()
#print(json.dumps(data, indent=2))
index = 0
for item in data['items']:
    video_url = 'https://www.youtube.com/watch?v=' + item['id']['videoId']
    print(json.dumps(video_url, indent=2))
    thumbnail_url = item['snippet']['thumbnails']['medium']['url']
    print(json.dumps(thumbnail_url, indent=2))
    index += 1
    urllib.request.urlretrieve(thumbnail_url, 'images/recent-video-' + str(index) + '.jpg')
    video_link = soup.find("a", {"id": "recent-video-" + str(index)})
    video_link['href'] = video_url

with open("index.html", "wb") as f_output:
    f_output.write(soup.prettify("utf-8"))