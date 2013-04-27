from script import ServerScript, CharacterScript, command
from stlib import constants

class CommandServer(ServerScript):
    def on_start(self):
        pass

    def on_stop(self):
        pass

def get_class():
    return CommandServer

@command
def kill(script):
    script.character.kill()