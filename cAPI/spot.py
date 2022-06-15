from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from typing_extensions import Self
import cAPI.apiList as api
import requests
import base64
import urllib

# Text to base64
def b64(text: str) -> str:
    text = text.encode('ascii')
    return base64.b64encode(text).decode('ascii')

API_ENDPOINT = "https://accounts.spotify.com/api/token"

class Spotify:
  def __init__(self, clientToken, privateToken,username):
    self.clientToken = clientToken
    self.privateToken = privateToken
    self.username = username

  def getAuthToken(self):
    r = requests.request(
            'POST',
            'https://accounts.spotify.com/api/token',
            data={
                'grant_type': 'client_credentials'
            },
            headers={'Authorization': 'Basic ' + b64(str(self.clientToken) + ':' + str(self.privateToken))}
        ).json()
    return r["access_token"]

  def getUsername(self):
    r = requests.get('https://api.spotify.com/v1/users/' + self.username, headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
    return r[api.display_name]

  def getFollowers(self):
    r = requests.get('https://api.spotify.com/v1/users/' + self.username, headers={'Authorization': 'Bearer ' + self.getAuthToken()}).json()
    return r[api.followers]["total"]


    








    








