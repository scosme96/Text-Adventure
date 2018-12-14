#Sandy Cosme
#Python Text Adventure

#imports several commands and functions needed.
import cmd
import sys
import os
import random

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
	def __init__(self, player):
		charecter.__init__(self)
		self.name = 'Kobald Leader'
		self.hp = 20

# this is the player setup
class Player:
    def __init__(self):
        Character.__init__(self)
        self.name = ''
        self.hp = 20
        self.location = 'starting_area'
        self.game_over = False

# Title Screen
# This chunk of code is for the tittle screen options
def title_screen_selections():
    option = input(">")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("Quit"):
        sys.exit()

#this is what shows when booting up the game/the title screen
def title_screen():
    os.system(cls)
    print("Welcome to a random python Text Adventure")
    print('Play')
    print('Help')
    print('Quit')
    title_screen_select()
#this is the help menu
def help_menu():
    print("Welcome to a random python Text Adventure")
    print('Type in your commands to do them')
    print('use look to inspect')
    title_screen_selections()



AREANAME = ''
DESCRIBE = 'describe'
EXAMINE = 'examine'
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
		DESCRIBE: 'This is the enterance to the cave.',
		EXAMINE: 'The enterance of the cave looks like any other normal cave',
		SOLVED: False,
		FORWARD: 'l2',
		DOWN: '',
		LEFT: '',
		RIGHT: '',
	},
	'l2': {
		AREANAME: 'Tunnel Corridor',
		DESCRIBE: 'This is tunnel leading further into the cave',
		EXAMINE: 'The tunnel is litered with signs of the kobald brigands there are totems, banners, and junk litering the area',
		SOLVED: False,
		FORWARD: 'l4',
		DOWN: 'l1',
		LEFT: 'l3',
		RIGHT: '',
	},
	'l3': {
		AREANAME: 'Store Room',
		DESCRIBE: 'This seems to be a store room for equipment the kolbolds use',
		EXAMINE: 'In the corner of the room you find a mid sized broadsword',
		SOLVED: False,
		FORWARD: '',
		DOWN: '',
		LEFT: '',
		RIGHT: 'l2',
	},
	'l4': {
		AREANAME: 'Cave Hideout',
		DESCRIBE: 'This is where the Kobolds hang out in when they are not out raiding and robbing the villagers',
		EXAMINE: 'The room is filled with tables, totems, and sleeping cots',
		SOLVED: False,
		FORWARD: 'l5',
		DOWN: 'l2',
		LEFT: '',
		RIGHT: '',
	},
		l5: {
		AREANAME: 'Cave Dungeon',
		DESCRIBE: 'These are the makeshift holding cells that the brigands where using to hold their captives',
		EXAMINE: 'You see the captued villagers you where sent to save being held inside the makeshift cells',
		SOLVED: False,
		FORWARD: '',
		DOWN: 'l4',
		LEFT: '',
		RIGHT: '',
	}
}

#this is the base class for Items in the game
class Items():
	def __init__(self, name, description):
		self.name = name
		self.description = description

#First key found in the game, unlocks the door to the storeroom.
class copper_key (Items):
	def __init__(self):
		self.name = copper_key
		self.description = 'a worn down key made of copper. Found on the dead Kobald'

#this the base class for weapons in the game
class Weapons(Items):
	def __init__(self, name, description, damage):
		self.damage = damage
		self.name = name
		self.description

#first weapon in the game, your starter weapon
class Dagger(Weapons):
	def __init__(self):
		self.damage = 3
	self.name = Dagger
	self.description = 'a dagger kept in good condition'


#this code print the curerent location the player charascter is in
def print_location():
	print('\n' + ('#' * (2 + len(player.location))))
	print('#' + player.location + '#')
	print('#' + areamap[player.position][DESCRIPTION] + "#")
	print('\n' + ('#' * (2 + len(player.location))))

#this code defines the prompts the player will recive to help them
def prompt():
	print("\n")
	print("What do you want to do?")
	action = input(">")
	acceptable_actions = ['move', 'go', 'quit', 'examine', 'take', 'look', 'inspect']
	while action.lower() not in acceptable_actions:
		print("Unknown command/action, please try again.\n")
		action = input(">")
	if action.lower() == 'quit':
		sys.exit()
	elif action.lower() in ['move', 'go']:
		player_move(action.lower())
	elif action.lower() in ['examine', 'look', 'inspect']:
		player_examine(actoin.lower)

#this code enable the player charecter to move around the map
def player_move(action):
	ask = "where do you wan to go?\n"
	area = raw_input(ask)
	if area in ['up', 'north']:
		destination = areamap[player.location][FORWARD]
		movement_director(destination)
	elif area in ['down', 'south']:
		destination = areamap[player.location][DOWN]
	elif area in ['left', 'west']:
		destination = areamap[player.location][LEFT]
	elif area in ['right', 'east']:
		destination = areamap[player.location][RIGHT]
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

def start_game():
	os('cls')
	## Charecter naming/ intro
	player.name = raw_input('What is the name of your character')
	story1 = "you are a adventurer who has recieved a quest to save some captured villagers from a kobald hideout"
	story2 = "you've managed to track them down to a cave in the forest near the village"
	story3 = "you are now in front of the enterance to the cave"

	print("Begin your quest now")
	main_game_loop()
