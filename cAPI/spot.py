from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from typing_extensions import Self
from unicodedata import name
import cAPI.apiList as api
import requests
import base64
import urllib
import time
import subprocess 

my_list = []

# phone = 2ae12c5a950bb4a132d3f3bed6384153fcbbf701
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
  
  def getCurrentPlayingTrackID(self):
    r = requests.get('https://api.spotify.com/v1/me/player/currently-playing?market=DE', headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
    item = r["item"]
    newItem = item["id"]
    return newItem




  
  def getPlaybackState(self):
      r = requests.get('https://api.spotify.com/v1/me/player', headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
      return r

  def getMusicStartinSeconds(self):
      r = requests.get('	https://api.spotify.com/v1/audio-analysis/' + self.getCurrentPlayingTrackID(), headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
      item = r["sections"][1]["start"]
      lastItem = float(item) - 2.00000
      return lastItem * 1000

  
  def StopMusic(self):
      r = requests.put('https://api.spotify.com/v1/me/player/pause?device_id=2ae12c5a950bb4a132d3f3bed6384153fcbbf701' + self.getCurrentPlayingTrackID(), headers={'Authorization': 'Bearer ' + self.getAuthToken()})
      return r
  
  def seekMusic(self):
      r = requests.put('https://api.spotify.com/v1/me/player/seek?position_ms=' + str(self.getMusicStartinSeconds()) + '&device_id=2ae12c5a950bb4a132d3f3bed6384153fcbbf701', headers={'Authorization': 'Bearer ' + self.getAuthToken()})
      return r

    



      


    

    

        









      






    








    








