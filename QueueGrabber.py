import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import random
import sys
from pprint import pprint

# Setup information for environment variables needed to run the API in the first place
os.environ["SPOTIPY_CLIENT_ID"]  = "72e6a8650c3d4cdea4f71d1a53d0ea32"
os.environ["SPOTIPY_CLIENT_SECRET"] = "5be64385f20e4079853687e2c92d7f48"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://example.com"
username = os.environ["SPOTIPY_CLIENT_ID"]

# Globals needed
BodyMin = 1800000
BodyMax = 1920000

# Playlist ID's
WorkoutBodyList = ''
WorkoutEndList = ''

def checkDuplicates(playlist, key): #Returns true if there is a duplicate, false otherwise
    return False

# generateBody()
#Function:
#   Takes the playlist for Workout General and randomly selects songs that belong in the queue. It randomly grabs a
#   song in the playlist, and then will attempt to add it to the queue list. Before, however, it will check for
#   duplicates to make sure that we don't have repeats because that is lame.
#Problems:
#
def generateBody(): #Must return a list of songs to be added to the queue. Prob needs ID's in list?
    failureTimer = 2
    queueList = []
    totalTime = 0
    playlist = sp.playlist_items(WorkoutBodyList)
    while True:   #Continue to loop until we find a good candidate
        #find us a song to try to add
        spot = random.randint(0, len(playlist['items']))
        info = [playlist['items'][spot]['track']['name'],
                playlist['items'][spot]['track']['uri'],
                playlist['items'][spot]['track']['duration_ms']]
        if not checkDuplicates(queueList, info):
            queueList.append(info) #Append the song
            totalTime += info[2]
        if totalTime > BodyMin and totalTime < BodyMax or failureTimer == 0:
            return queueList
        failureTimer-=1
    return queueList

def generateFinish(): #must return a single song to be added to the queue. Prob ID again
    pass

############################# Main ###############################
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
playlistname = sp.playlist(WorkoutBodyList)['name']
playlist = sp.playlist_items(WorkoutBodyList)
print("Playlist \""+ playlistname+ "\" contains", len(playlist['items']), "songs.")

for i in range(len(playlist['items'])):
    print(playlist['items'][i]['track']['duration_ms'])

queueList = generateBody()
pprint(queueList)
