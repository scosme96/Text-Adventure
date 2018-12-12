#Sandy Cosme
#Python Text Adventure

import cmd
import textwrap
import sys
import os
import random
screen_width = 100


#This code creates a class for charecters
class Character:
    def  __init__(self):
        self.name = ""

# This piece of code creates an Enemy class
class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = 'Kobolt'
# this is the player setup
class Player:
    def __init__(self):
        Character.__init__(self)
        self.name = ''
        self.hp = 0
        self.location = 'starting area'
        mcplayer = player()





#### Title Screen ####
# This chunk of code is for the tittle screen options
def title_screen_selections():
    option = input(">")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
