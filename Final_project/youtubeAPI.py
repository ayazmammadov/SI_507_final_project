

#from apiclient.discovery import build
from googleapiclient import discovery
import googleapiclient.discovery
from googleapiclient.discovery import build
from secrets import youtube_key

import json
import requests
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
base_url = 'https://www.youtube.com/watch?v='

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey = youtube_key )

def searchYoutube(searchitem):
    response = getattr(youtube, 'search')().list(part='snippet', q = searchitem, type='video', maxResults = 1).execute()
    movie_id = response['items'][0]['id']['videoId']
    youtube_url = base_url + movie_id
    
    return youtube_url

