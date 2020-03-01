#!/bin/python3

# IT101 - RPG dungeon game project
# Jordan Golden

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Navigate your way through the Deadmines and
thwart the Defias Brotherhood.  Defeat the
bosses and get to the exit with their loot.

Commands:
  go [direction]
  get [item]
  attack monster
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print a monster if there is one
  if "monster" in rooms[currentRoom]:
    print('There is a monster in the room: ' + rooms[currentRoom]['monster'])
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Mine Entrance' : {
                  'south' : 'Ironclad Cove'
                },

            'Ironclad Cove' : {
                  'north' : 'Mine Entrance',
                  'east' : 'Mineshaft 1',
                  'monster' : 'Rhahk\'zor',
                  'item' : 'rhahk\'zor\'s_hammer'
                },

            'Mineshaft 1' : {
                    'west' : 'Ironclad Cove',
                    'south' : 'Mast Room'
                },

            'Mast Room' : {
                    'north' : 'Mineshaft 1',
                    'east' : 'Mineshaft 2',
                    'monster' : 'Sneed',
                    'item' : 'buzzsaw'
                },

            'Mineshaft 2' : {
                    'west' : 'Mast Room',
                    'north' : 'Goblin Foundry'
                },

            'Goblin Foundry' : {
                    'south' : 'Mineshaft 2',
                    'north' : 'Powder Room',
                    'monster' : 'Gilnid',
                    'item'  : 'lavishly_jeweled_ring'
                },

            'Powder Room' : {
                    'south' : 'Goblin Foundry',
                    'east' : 'Dank Cove',
                    'item' : 'powder_barrel'
                },

            'Dank Cove' : {
                    'west' : 'Powder Room',
                    'east' : 'Dreadnought'
                },

            'Dreadnought' : {
                    'west' : 'Dank Cove',
                    'up' : 'Dreadnought Cabin',
                    'monster' : 'Mr. Smite',
                    'item' : 'smite\'s_hammer'
                },

            'Dreadnought Cabin' : {
                    'down' : 'Dreadnought',
                    'east' : 'Mine Exit',
                    'monster' : 'Edwin van Cleef',
                    'item' : 'unsent_letter'
                },

            'Mine Exit' : { 'west' : 'Dreadnought Cabin' }
         }

#start the player in the dungeon entrance
currentRoom = 'Mine Entrance'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print('You got ' + move[1] + '.')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')


  if move[0] == 'attack' and move[1] == 'monster':
    if "monster" in rooms[currentRoom]:
        print('Monster is defeated!')
        del rooms[currentRoom]['monster']

    else:
        print('Nothing to attack here.')

  # player wins if they get to the exit with the unsent letter
  if currentRoom == 'Mine Exit' and 'unsent_letter' in inventory:
    print('You beat the dungeon... YOU WIN!')
    break