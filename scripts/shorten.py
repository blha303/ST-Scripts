from script import ServerScript, CharacterScript, command
from stlib import constants

from util import http, web

class CommandServer(ServerScript):
    def on_start(self):
        pass

    def on_stop(self):
        pass

def get_class():
    return CommandServer

@command
def shorten(script, one):
    try:
        script.character.send_chat("[shorten] " + web.isgd(one))
    except (web.ShortenError, http.HTTPError) as error:
        script.character.send_chat("/shorten: " + error)

print "[Shorten] Link shortener script loaded"
