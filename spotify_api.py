import urllib.parse
import pkce
import requests
from datetime import datetime, timedelta
import os
import base64
from dotenv import load_dotenv
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

def get_playlist(access_token):
    headers = {
            'Authorization': f"Bearer {access_token}"
    }
    response = requests.get(API_BASE_URL + "me/player/recently-played", headers=headers)
        
    playlist = response.json()
    audio_names = {}
    for i in range(10):
        artist = playlist['items'][i]['track']['album']['artists'][0]['name']
        title = playlist['items'][i]['track']['name']
        audio_names[i] = {'artist': artist,
                        'title': title}     
    return audio_names

def use_refresh_token(refresh_token):
    req_body = {
        'grant_type' : 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=req_body)
    return response.json()
