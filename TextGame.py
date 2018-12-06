#Sandy Cosme
#Python Text Adventure

#imports several commands and functions needed.
import cmd
import textwrap
import sys
import os
import random

screen_width = 100



#This code creates a base class for charecters
class Character:
    def  __init__(self):
        self.name = ""

# This piece of code creates an Enemy class
class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = 'Kobold'
        self.hp = 10
# Creates a class for the boss of the hideout
class Boss(Character):
	def __init__(self, player)
		charecter.__init__(self)
		self.name = 'Kobald Leader'
		self.hp = 20

# this is the player setup#####
class Player:
    def __init__(self):
        Character.__init__(self)
        self.name = ''
        self.hp = 20
        self.location = 'starting_area'
        self.game_over = False
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
    while option.lower() not in ['play', 'help', 'quit']:
        Print("Enter a valid command dumbo")
        option = input(">")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

#this is what shows when booting up the game/the title screen
def title_screen():
    os.system(cls)
    print('################')
    print("Welcome to a random python Text Adventure")
    print('####################')
    print('      -- Play --           ')
    print('      -- Help --           ')
    print('      -- Quit --           ')
    title_screen_selections()
#this is the help menu
def help_menu():
    print('################')
    print("Welcome to a random python Text Adventure")
    print('####################')
    print('Type in your commands to do them')
    print('use look to inspect')
    print('use the command attack fight enemies')
    title_screen_selections()



AREANAME = ''
DESCRIPTION = 'describe'
EXAMINATION = 'examine'
SOLVED = False
FORWARD = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

# list of all the rooms in the game
solved_areas = {'l1': False, 'l2': False, 'l3': False, 'l4':False, 'l5':False} 

#This code maps out and connects the differant rooms in the game
areamap = {
	'l1': {
		AREANAME: 'Cave Enterance',
		DESCRIPTION: 'This is the enterance to the cave.',
		EXAMINATION: 'The enterance of the cave looks like any other normal cave',
		SOLVED: False,
		FORWARD: 'l2',
		DOWN: '',
		LEFT: '',
		RIGHT: '',
	}
	'l2': {
		AREANAME: 'Tunnel Corridor',
		DESCRIPTION: 'This is tunnel leading further into the cave',
		EXAMINATION: 'The tunnel is litered with signs of the kobald brigands there are totems, banners, and junk litering the area',
		SOLVED: False,
		FORWARD: 'l4',
		DOWN: 'l1',
		LEFT: 'l3',
		RIGHT: '',
	}
	'l3': {
		AREANAME: 'Store Room',
		DESCRIPTION: 'This seems to be a store room for equipment the kolbolds use',
		EXAMINATION: 'In the corner of the room you find a mid sized broadsword',
		SOLVED: False,
		FORWARD: '',
		DOWN: '',
		LEFT: '',
		RIGHT: 'l2',
	}
	'l4': {
		AREANAME: 'Cave Hideout',
		DESCRIPTION: 'This is where the Kobolds hang out in when they are not out raiding and robbing the villagers',
		EXAMINATION: 'The room is filled with tables, totems, and sleeping cots',
		SOLVED: False,
		FORWARD: 'l5',
		DOWN: 'l2',
		LEFT: '',
		RIGHT: '',
	}	
		l5': {
		AREANAME: 'Cave Dungeon',
		DESCRIPTION: 'These are the makeshift holding cells that the brigands where using to hold their captives',
		EXAMINATION: 'You see the captued villagers you where sent to save being held inside the makeshift cells',
		SOLVED: False,
		FORWARD: '',
		DOWN: 'l4',
		LEFT: '',
		RIGHT: '',
	}
}	

#this is the base class for Items in the game
class Items():
	def __init__(self, name, description)
		self.name = name
		self.description = description

#First key found in the game, unlocks the door to the storeroom.
class copper key(Items):
	def __init__(self):
		self.name = copper key
		self.description = 'a worn down key made of copper. Found on the dead Kobald'

#this the base class for weapons in the game
class Weapons(Items):
	def __init__(self, name, description, damage):
		self.damage = damage
		self.name = name
		self.description

#first weapon in the game, your starter weapon
class Dagger(Weapons):
	def __init__(self)
	self.damage = 3
	self.name = Dagger
	self.description = 'a dagger kept in good condition'  



def print_location():
	print('\n' + ('#' * (2 + len(mcplayer.location))))
	print('#' + mcplayer.location + '#')
	print('#' + areamap[mcplayer.position][DESCRIPTION] + "#")
	print('\n' + ('#' * (2 + len(mcplayer.location))))

#this code defines the prompts the player will recive to help them
def prompt():
	print("\n##############")
	print("What do you want to do?")
	action = input(">")
	acceptable_actions = ['move', 'go', 'quit', 'examine', 'take', 'look', 'inspect']
	while action.lower() not in acceptable_actions:
		print("Unknown command/action, please try again.\n")
		action = input(">")
	if action.lower() == 'quit':
		sys.exit()
	elif action.lower() in ['move', 'go']
		player_move(action.lower())
	elif action.lower() in ['examine', 'look', 'inspect']
		player_examine(actoin.lower)

#this code enable the player charecter to move around the map
def player_move(pAction):
	ask = "where do you wan to go?\n"
	area = input(ask)
	if area in ['up', 'north']:
		destination = areamap[mcplayer.location][FORWARD]
		movement_director(destination)
	elif area in ['down', 'south']:
		destination = areamap[mcplayer.location][DOWN]
	elif area in ['left', 'west']:
		destination = areamap[mcplayer.location][LEFT]
	elif area in ['right', 'east']:
		destination = areamap[mcplayer.location][RIGHT]
#this code prints the location and informs the player when they move
def movement_director(destination):
	print("\n" + "You moved to the" + destination + ".")
	print_location()

#code enables the player to examine rooms
def player_examine(action):
	if areamap[mplayer.location][SOLVED]:
		print("you have already taken every item avalable in this room")
	else :
		print("there are still some items of use here")

#this keeps the game 
def main_game_loop():
	while myplayer.game_over == False:
		prompt()
		#when all enemies have been defeated and keys found.

def start_game():
	os.('cls')
	## Charecter naming/ intro
	question = "What is your charecters name?\n"
	mcplayer.name = input(">")
	
	talk1 = "you are a adventurer who has recieved a quest to save some captured villagers from a kobald hideout:
	talk2 = "you've managed to track them down to a cave in the forest near the village"
	talk3 = "you are now in front of the enterance to the cave"
	
	print("Begin your quest now")
	main_game_loop()

title_screen()
