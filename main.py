from cAPI.spot import Spotify
import json

with open('config.json') as json_file:
         data = json.load(json_file)


p1 = Spotify(data["publicKey"], data["privateKey"])

print(p1.getAuthToken())
