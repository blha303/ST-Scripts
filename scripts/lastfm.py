from script import ServerScript, CharacterScript, command
from stlib import constants
from util import http, timesince
from datetime import datetime

api_url = "http://ws.audioscrobbler.com/2.0/?format=json"
api_key = "8b651d90ec0b645fb22b4f5765a87790"
print "[LastFm] Lastfm script starting"

class CommandServer(ServerScript):
    def on_start(self):
        pass

    def on_stop(self):
        pass

def get_class():
    return CommandServer

@command
def lastfm(script):
    if not api_key:
        script.character.send_chat("[lastfm] error: no api key set")

    user = script.character.name

    response = http.get_json(api_url, method="user.getrecenttracks",
                             api_key=api_key, user=user, limit=1)

    if 'error' in response:
        script.character.send_chat("[lastfm] Error: %s." % response["message"])

    if not "track" in response["recenttracks"] or len(response["recenttracks"]["track"]) == 0:
        script.character.send_chat('[lastfm] No recent tracks for user "%s" found.' % user

    tracks = response["recenttracks"]["track"]

    if type(tracks) == list:
        # if the user is listening to something, the tracks entry is a list
        # the first item is the current track
        track = tracks[0]
        status = 'is listening to'
        ending = '.'
    elif type(tracks) == dict:
        # otherwise, they aren't listening to anything right now, and
        # the tracks entry is a dict representing the most recent track
        track = tracks
        status = 'last listened to'
        # lets see how long ago they listened to it
        time_listened = datetime.fromtimestamp(int(track["date"]["uts"]))
        time_since = timesince.timesince(time_listened)
        ending = ' (%s ago)' % time_since

    else:
        script.character.send_chat("[lastfm] error: could not parse track listing"

    title = track["name"]
    album = track["album"]["#text"]
    artist = track["artist"]["#text"]

    out = '%s %s "%s"' % (user, status, title)
    if artist:
        out += " by \x02%s\x0f" % artist
    if album:
        out += " from the album \x02%s\x0f" % album

    # append ending based on what type it was
    out += ending

    script.character.send_chat("[lastfm] " + out)

print "[LastFm] Lastfm script loaded"
