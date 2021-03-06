#Hunt the Wumpus
#From a vintage BASIC game program
#by CREATIVE COMPUTING MORRISTOWN, NEW JERSEY
#Rewritten in Python by Gordon Reeder
# Python 3.4
# ** To do **
# - Make connections within cave random. So that no two caves are the same.

import random
import sys

def show_instructions():
    print ("""
        WELCOME TO 'HUNT THE WUMPUS'
        THE WUMPUS LIVES IN A CAVE OF 16 ROOMS.
        13 14 15 16
        9  10 11 12
        5  6  7  8
        1  2  3  4
        
    WARNINGS:
        WHEN YOU ARE ONE ROOM AWAY FROM WUMPUS OR A HAZARD,
        THE COMPUTER SAYS:
        WUMPUS:   'STENCH'
        PIT   :   'BREEZE'
        """)


class Room:
    """Defines a room. 
    A room has a name (or number),
    a list of other rooms that it connects to.
    and a description. 
    How these rooms are built into something larger 
    (cave, dungeon, skyscraper) is up to you.
    """

    def __init__(self, **kwargs):
        self.number = 0
        self.name =''
        self.connects_to = [] #These are NOT objects
        self.description = ""
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __str__(self):
        return str(self.number)

    def remove_connect(self, arg_connect):
        if arg_connect in self.connects_to:
            self.connects_to.remove(arg_connects)

    def add_connect(self, arg_connect):
        if arg_connect not in self.connects_to:
            self.connects_to.append(arg_connect)

    def is_valid_connect(self, arg_connect):
        return arg_connect in self.connects_to

    def get_number_of_connects(self):
        return len(self.connects_to)

    def get_connects(self):
        return self.connects_to

    def describe(self):
        if len(self.description) > 0:
            print(self.description)
        else:
            print("You are in room {}.\nPassages lead to {}".format(self.number, self.connects_to))
        

class Thing:
    """Defines the things that are in the cave.
    That is the Wumpus, Player, pits and gold.
    """

    def __init__(self, **kwargs):
        self.location = 0 # this is a room object
        for key, value in kwargs.items():
            setattr(self, key, value)

    def move(self, a_new_location):
        if a_new_location.number in self.location.connects_to or a_new_location == self.location:
            self.location = a_new_location
            return True
        else:
            return False

    def validate_move(self, a_new_location):
        return a_new_location.number in self.location.connects_to or a_new_location == self.location
                
    def get_location(self):
        return self.location.number

    def wakeup(self, a_cave):
        if random.randint(0, 3): # P=.75 that we will move.
            self.location = a_cave[random.choice(self.location.connects_to) -1]
 
    def is_hit(self, a_room):
        return self.location == a_room

def create_things(a_cave):
    # a_cave = room, 0 - 15
    Things=[]
    Things.append(Thing(location = a_cave[0])) # Player berada di kolom 1.1
    checker = False

    while checker == False:
        Samples = random.sample(a_cave, 5) #Wumpus, Pit1, Pit2, Pit3, Gold
        Pits = [Samples[1], Samples[2], Samples[3]]
        forbiddenRoom1 = [a_cave[1], a_cave[4]]
        forbiddenRoom2 = [a_cave[2], a_cave[7]]
        forbiddenRoom3 = [a_cave[13], a_cave[8]]
        forbiddenRoom4 = [a_cave[11], a_cave[14]]
    
        checker = True
        
        if Samples[0] == a_cave[0]:
            checker = False
        if Samples[1] == a_cave[0] or Samples[2] == a_cave[0] or Samples[3] == a_cave[0]:
            checker = False
        if (len(set(forbiddenRoom1) - set(Pits)) == 0):
            checker = False
        if (len(set(forbiddenRoom2) - set(Pits)) == 0):
            checker = False
        if (len(set(forbiddenRoom3) - set(Pits)) == 0):
            checker = False

    for room in Samples:
        Things.append(Thing(location = room))

    return Things

def create_cave():
    # First create a list of all the rooms.
    for number in range(16):
        Cave.append(Room(number = number +1))

    # Then stich them together.
    for idx, room in enumerate(Cave):
        #connect to room to the right
        if idx != 0:
            if idx != 4:
                if idx != 8:
                 if idx != 12:
                    room.add_connect(Cave[idx -1].number)
        if idx == 15:
            room.add_connect(Cave[11].number)
        elif idx == 3:
            ''
        elif idx == 7:
            ''
        elif idx == 11:
            ''
        else:    
            room.add_connect(Cave[idx +1].number) 

        #connect to room up or down
        if idx == 0:
            room.add_connect(5)
        if idx == 1:
            room.add_connect(6)
        if idx == 2:
            room.add_connect(7)
        if idx == 3:
            room.add_connect(8)
        if idx == 4:
            room.add_connect(1)
            room.add_connect(9)
        if idx == 5:
            room.add_connect(2)
            room.add_connect(10)
        if idx == 6:
            room.add_connect(3)
            room.add_connect(11)
        if idx == 7:
            room.add_connect(4)
            room.add_connect(12)
        if idx == 8:
            room.add_connect(5)
            room.add_connect(13)
        if idx == 9:
            room.add_connect(6)
            room.add_connect(14)
        if idx == 10:
            room.add_connect(7)
            room.add_connect(15)
        if idx == 11:
            room.add_connect(8)
            room.add_connect(16)
        if idx == 12:
            room.add_connect(9)
        if idx == 13:
            room.add_connect(10)
        if idx == 14:
            room.add_connect(11)

# ============ BEGIN HERE ===========

Cave = []
create_cave()
# Make player, wumpus, pits and put into cave.

Player, Wumpus, Pit1, Pit2, Pit3, Gold = create_things(Cave)

Arrows = 5

# Now play the game

print("""\n 
13 14 15 16
9  10 11 12
5  6  7  8
1  2  3  4
        \n
    Welcome to the cave, Great White Hunter.
    You are hunting the Wumpus.
    On any turn you can move or shoot.
    Commands are entered in the form of ACTION LOCATION
    IE: 'SHOOT 12' or 'MOVE 8'
    type 'HELP' for instructions.
    'QUIT' to end the game.
    """)


while True:
    Player.location.describe()
    #Check each <Player.location.connects_to> for hazards.
    for room in Player.location.connects_to:
        if Wumpus.location.number == room:
            print("Stench")
        if Pit1.location.number == room or Pit2.location.number == room:
            print("Breeze")
       
    if Gold.location.number == room:
        print("Gold Found. Press T to take the gold")
    raw_command = input("\n> ")
    command_list = raw_command.split(' ')
    command = command_list[0].upper()
    if len(command_list) > 1:
        try:
            move = Cave[int(command_list[1]) -1]
        except:
            print("\n **What??")
            continue
    else:
        move = Player.location
    if command == 'TAKE' or command == 'T':
            # TODO : TAKE GOLD ACTION
            continue
    if command == 'HELP' or command == 'H':
        show_instructions()
        continue

    elif command == 'QUIT' or command == 'Q':
        print("\nOK, Bye.")
        sys.exit()

    elif command == 'MOVE' or command == 'M':
        if Player.move(move):
            if Player.location == Wumpus.location:
                print("... OOPS! BUMPED A WUMPUS!")
        else:
            print("\n **You can't get there from here")
            continue

    elif command == 'SHOOT' or command == 'S':
        if Player.validate_move(move):
            print("\n-Twang-") 
            if Wumpus.location == move:
                print("\n Good Shooting!! You hit the Wumpus. \n Wumpi will have their revenge.\n")
                sys.exit()
        else:
            print("\n** Stop trying to shoot through walls.")

        Wumpus.wakeup(Cave)
        Arrows -= 1
        if Arrows == 0:
            print("\n You are out of arrows\n Better luck next time\n")
            sys.exit()
    
    else:
        print("\n **COMMAND YANG TERSEDIA : \n 1. MOVE {ANGKA} \n 2. SHOOT {ANGKA} \n 3. HELP \n 4. QUIT")
        continue

        
    # By now the player has moved. See what happened.
    # Handle problems with pits, bats and wumpus.

    if Player.location == Wumpus.location:
        print("Wumpus Memakanmu\n")
        sys.exit()    

    elif Player.location == Pit1.location or Player.location == Pit2.location or Player.location == Pit3.location:
        print("Anda masuk kedalam PIT\n")
        sys.exit()

    else: # Keep playing
        pass
