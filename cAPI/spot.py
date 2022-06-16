from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from typing_extensions import Self
import cAPI.apiList as api
import requests
import base64
import urllib
import time
import subprocess 

# Text to base64
def b64(text: str) -> str:
    text = text.encode('ascii')
    return base64.b64encode(text).decode('ascii')

API_ENDPOINT = "https://accounts.spotify.com/api/token"

class Spotify:
  def __init__(self, clientToken, privateToken,refreshToken,username):
    self.clientToken = clientToken
    self.privateToken = privateToken
    self.refreshToken = refreshToken
    self.username = username

  def getAuthToken(self):
    r = requests.request(
            'POST',
            'https://accounts.spotify.com/api/token',
            data={
                'grant_type': 'refresh_token',
                'refresh_token': self.refreshToken,
                'client_id': self.clientToken,
                'client_secret': self.privateToken
          
            },
        ).json()
    return r['access_token']

  def getUsername(self):
    r = requests.get('https://api.spotify.com/v1/users/' + self.username, headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
    return r[api.display_name]

  def getFollowers(self):
    r = requests.get('https://api.spotify.com/v1/users/' + self.username, headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
    return r[api.followers]["total"]

  def isImage(self):
    r = requests.get('https://api.spotify.com/v1/users/' + self.username, headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
    is_image = r[api.images]
    if len(is_image) != 0:
       return True


  def getImage(self):
    r = requests.get('https://api.spotify.com/v1/users/' + self.username, headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
    if self.isImage():
       return r[api.images][0]["url"]
    else:
      return False
  
  def getCurrentPlayingSong(self):
    r = requests.get('https://api.spotify.com/v1/me/player/currently-playing?market=DE', headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
    item = r["item"]
    newItem = item["name"]
    return newItem

  def getCurrentPlayingTrackAuthor(self):
    r = requests.get('https://api.spotify.com/v1/me/player/currently-playing?market=DE', headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
    item = r["item"]
    newItem = item["album"]
    lastItem = newItem["artists"][0]["name"]
    return lastItem


      






    








    








