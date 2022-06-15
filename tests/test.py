from cAPI.spot import Spotify
import json
import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

USERNAME = "31epp5skpbyfnjrcs5pde6xx3cle"

with open('config.json') as json_file:
         data = json.load(json_file)

p1 = Spotify(data["publicKey"], data["privateKey"], USERNAME)

def checkUsername():
    a = datetime.datetime.now()
    user = "Script"
    if p1.getUsername() == user:
        b = datetime.datetime.now()
        delta = b - a
        return bcolors.OKBLUE + "SUCCESS in " + str(delta) + bcolors.OKGREEN + " REAL NAME OUTPUT: " + user
    else:
        b = datetime.datetime.now()
        delta = b - a
        return bcolors.FAIL + "ERROR in " + str(delta) + bcolors.WARNING + " EXPECTED OUTPUT: " + p1.getUsername() + bcolors.FAIL + " REAL NAME  OUTPUT: " + user


def checkFollowers():
    a = datetime.datetime.now()
    follower = 1
    if p1.getFollowers() == follower:
        b = datetime.datetime.now()
        delta = b - a
        return bcolors.OKBLUE + "SUCCESS in " + str(delta) + bcolors.OKGREEN + " REAL FOLLOWER OUTPUT: " + str(follower)
    else:
        b = datetime.datetime.now()
        delta = b - a
        return bcolors.FAIL + "ERROR in " + str(delta) + bcolors.WARNING + " EXPECTED OUTPUT: " + str(p1.getFollowers()) + bcolors.FAIL + " REAL FOLLOWER  OUTPUT: " + str(follower)



def runTests():
    print(checkUsername()) # username check

    print(checkFollowers()) # follower check




