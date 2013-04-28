from script import ServerScript, CharacterScript, command
from stlib import constants

def prompt_for_password(character):
    character.send_chat('You need to login. /login <password>')

class CommandServer(ServerScript):
    def on_start(self):
        pass

    def on_stop(self):
        pass

    def on_character_created(self, character):
        if character.name in cfg_logins:
            

def get_class():
    return CommandServer

@command
def login(script, arg):
    
