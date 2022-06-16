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
PLAYING_SONG =  "DOTY" # CHANGE
CURRENT_AUTHOR = "KALIM" # CHANGE

TEST_STATUS = 0
with open('config.json') as json_file:
         data = json.load(json_file)

p1 = Spotify(data["publicKey"], data["privateKey"], data["refleshKey"],USERNAME)


    
def checkUsername():

    global TEST_STATUS
    a = datetime.datetime.now()
    user = "Script"
    if p1.getUsername() == user:
        b = datetime.datetime.now()
        delta = b - a

        TEST_STATUS += 1
        return bcolors.OKBLUE + "SUCCESS in " + str(delta) + bcolors.OKGREEN + " REAL NAME OUTPUT: " + user
    else:
        b = datetime.datetime.now()
        delta = b - a
        return bcolors.FAIL + "ERROR in " + str(delta) + bcolors.WARNING + " EXPECTED OUTPUT: " + p1.getUsername() + bcolors.FAIL + " REAL NAME  OUTPUT: " + user


def checkFollowers(): # TODO: SOMETIMES IT CANT COMPARE THE FOLLOWERS
    global TEST_STATUS
    a = datetime.datetime.now()
    follower = 0
    if p1.getFollowers() == follower:
        b = datetime.datetime.now()
        delta = b - a
        TEST_STATUS += 1
        return bcolors.OKBLUE + "SUCCESS in " + str(delta) + bcolors.OKGREEN + " REAL FOLLOWER OUTPUT: " + str(follower)
    else:
        b = datetime.datetime.now()
        delta = b - a
        return bcolors.FAIL + "ERROR in " + str(delta) + bcolors.WARNING + " EXPECTED OUTPUT: " + str(p1.getFollowers()) + bcolors.FAIL + " REAL FOLLOWER  OUTPUT: " + str(follower)


def checkImage():
    global TEST_STATUS
    a = datetime.datetime.now()
    if p1.isImage():
        b = datetime.datetime.now()
        delta = b - a
        TEST_STATUS += 1
        return bcolors.OKBLUE + "SUCCESS in " + str(delta) + bcolors.OKGREEN + " REAL URL: " + p1.getImage()
    else:
        b = datetime.datetime.now()
        delta = b - a
        return bcolors.FAIL + "ERROR in " + str(delta) + bcolors.FAIL + " NO IMAGE: "

def checkCurrentPlayingSong():
    global TEST_STATUS
    a = datetime.datetime.now()
    if p1.getCurrentPlayingSong() == "DOTY":
        b = datetime.datetime.now()
        delta = b - a
        TEST_STATUS += 1
        return bcolors.OKBLUE + "SUCCESS in " + str(delta) + bcolors.OKGREEN + " SONG NAME: " + p1.getCurrentPlayingSong()
    else:
        b = datetime.datetime.now()
        delta = b - a
        return bcolors.FAIL + "ERROR in " + str(delta) + bcolors.WARNING + " EXPECTED OUTPUT: " + PLAYING_SONG + bcolors.FAIL + " REAL FOLLOWER  OUTPUT: " + p1.getCurrentPlayingSong()


def checkCurrentAuthor():
    global TEST_STATUS
    a = datetime.datetime.now()
    if p1.getCurrentPlayingTrackAuthor() == "KALIM":
        b = datetime.datetime.now()
        delta = b - a
        TEST_STATUS += 1
        return bcolors.OKBLUE + "SUCCESS in " + str(delta) + bcolors.OKGREEN + " AUTHOR NAME: " + p1.getCurrentPlayingTrackAuthor()
    else:
        b = datetime.datetime.now()
        delta = b - a
        return bcolors.FAIL + "ERROR in " + str(delta) + bcolors.WARNING + " EXPECTED OUTPUT: " + CURRENT_AUTHOR + bcolors.FAIL + " REAL FOLLOWER  OUTPUT: " + p1.getCurrentPlayingTrackAuthor()




def runTests():
    a = datetime.datetime.now()
    print(checkUsername()) # username check

    print(checkFollowers()) # follower check

    print(checkImage()) # image check TODO: RETURNS NONE ALTOUGHT ITS WORKING

    print(checkCurrentPlayingSong()) # get current playing song

    print(checkCurrentAuthor()) # get current playing song author

    if TEST_STATUS == 5:
        b = datetime.datetime.now()
        delta = b - a
        print(bcolors.OKCYAN + "ALL TESTS WERE SUCCESFULLY in " + bcolors.OKBLUE + str(delta))
    else:
        b = datetime.datetime.now()
        delta = b - a
        print(bcolors.FAIL + "ALL TESTS WERE NOT SUCCESFULLY in " + str(delta))







