from random import shuffle
import pygame
import sys
from random import randint
import random
import string
import sys, os


#import required libraries.



pygame.font.init()
#initalise pygame font

my_font2 = pygame.font.SysFont('Arial', 27, bold=True)
my_font = pygame.font.SysFont('Arial', 20)

#initialise pygame fonts.




#define required colours.
CREAM = (246, 245, 231)
BEIGE = (175, 171, 140)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DGREEN = (89, 134, 85)
RED = (255, 0, 0)



colArr=[]
rowArr=[]
#define column array and row array
#these hold the locations of the letters that are placed onto the board respectively.

tileArr=[]
#tilearray is an array which holds the letters which are placed onto the board.

boardWords=[]
#boardWords is an array which holds the words that are sucessfully placed onto the board.


            
# Defines width and height of grid locations.

WIDTH = 45
HEIGHT = 45
# Defines integers width and height of grid locations.


ADDERx=580
ADDERy=202
#Integer variables which allowed the manipulation of the resolution
#to fullscreen easily.

########################### BOARD CREATION ###########################
 
#Distance between each cell.
MARGIN = 5
 
#Creation of the two-dimensional array to represent the scrabble board.

grid = []
for row in range(15):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(15):
        grid[row].append(0)  # Append a cell
 

grid[1][10] = 1
#grid array
 
# Initialize pygame
pygame.init()
 
#Window size for pygame 
WINDOW_SIZE = [1920, 1080]
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
 
#Set title for screen
pygame.display.set_caption("Scrabble Game")
 
done = False
 
# pygame in-built function to adjust frames per second of the screen.
clock = pygame.time.Clock()


#Dictionary data structure to assign each letter of the alphabet with a score value.

LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10
                 }

class Tile:
    def __init__(self, letter, letter_values):
        #Constructor method for the tile class.
        self.letter = letter.upper()
        if self.letter in letter_values:
            self.score = letter_values[self.letter]
        else:
            self.score = 0

    def get_letter(self):
        #Returns the string value of the letter of the tile.
        return self.letter

    def get_score(self):
        #Returns the value of the score of the specified player.
        return self.score

class Bag:
    def __init__(self):
        #Constructor for the bag class.
        self.bag = []
        self.initialize_bag()

    def add_to_bag(self, tile, quantity):
        #Adds a certain quantity of a certain tile to the bag. Takes a tile and an integer quantity as arguments.
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        #Adds the intiial 100 tiles to the bag.
        global LETTER_VALUES
        self.add_to_bag(Tile("A", LETTER_VALUES), 9)
        self.add_to_bag(Tile("B", LETTER_VALUES), 2)
        self.add_to_bag(Tile("C", LETTER_VALUES), 2)
        self.add_to_bag(Tile("D", LETTER_VALUES), 4)
        self.add_to_bag(Tile("E", LETTER_VALUES), 12)
        self.add_to_bag(Tile("F", LETTER_VALUES), 2)
        self.add_to_bag(Tile("G", LETTER_VALUES), 3)
        self.add_to_bag(Tile("H", LETTER_VALUES), 2)
        self.add_to_bag(Tile("I", LETTER_VALUES), 9)
        self.add_to_bag(Tile("J", LETTER_VALUES), 9)
        self.add_to_bag(Tile("K", LETTER_VALUES), 1)
        self.add_to_bag(Tile("L", LETTER_VALUES), 4)
        self.add_to_bag(Tile("M", LETTER_VALUES), 2)
        self.add_to_bag(Tile("N", LETTER_VALUES), 6)
        self.add_to_bag(Tile("O", LETTER_VALUES), 8)
        self.add_to_bag(Tile("P", LETTER_VALUES), 2)
        self.add_to_bag(Tile("Q", LETTER_VALUES), 1)
        self.add_to_bag(Tile("R", LETTER_VALUES), 6)
        self.add_to_bag(Tile("S", LETTER_VALUES), 4)
        self.add_to_bag(Tile("T", LETTER_VALUES), 6)
        self.add_to_bag(Tile("U", LETTER_VALUES), 4)
        self.add_to_bag(Tile("V", LETTER_VALUES), 2)
        self.add_to_bag(Tile("W", LETTER_VALUES), 2)
        self.add_to_bag(Tile("X", LETTER_VALUES), 1)
        self.add_to_bag(Tile("Y", LETTER_VALUES), 2)
        self.add_to_bag(Tile("Z", LETTER_VALUES), 1)
        #self.add_to_bag(Tile("#", LETTER_VALUES), 2)
        shuffle(self.bag)

    def take_from_bag(self):
        #Removes tile from the bag and returns it to user, used for replenishing tile-rack.
        return self.bag.pop()

    def get_remaining_tiles(self):
        #Returns integer number of tiles left in bag.
        return len(self.bag)

class Rack:
    def __init__(self, bag):
       #Initialise rack class.
        self.rack = []
        self.bag = bag
        self.initialize()

    def add_to_rack(self):
        #Takes tile from the bag and adds it to the rack.
        self.rack.append(self.bag.take_from_bag())

    def initialize(self):
        #Adds 7 letters to the rack.
        for i in range(7):
            self.add_to_rack()

    def get_rack_str(self):
        #Returns string of the rack of the current user.
        return ", ".join(str(item.get_letter()) for item in self.rack)
    
    def get_rack_list(self):
        #Returns the rack of the current user in list form.
        letterlist=[]
        for item in self.rack:
            letterlist.append(str(item.get_letter()))
        return letterlist
        

    def get_rack_arr(self):
        #Returns the rack of the current user as a list of tile class objects.
        return self.rack

    def remove_from_rack(self, tile):
        #Removes a tile from the rack for the current user.
        self.rack.remove(tile)

    def get_rack_length(self):
        #Returns the number of tiles left in the rack as an integer.
        return len(self.rack)

    def replenish_rack(self):
        #Makes sure the current user has 7 letters.
        while self.get_rack_length() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_to_rack()

class Player:
    def __init__(self, bag):
        #Constructor method for the player class, creates an instance of the rack class for each user.
        self.name = ""
        self.rack = Rack(bag)
        self.score = 0

    def set_name(self, name):
        #Sets the name for the player.
        self.name = name

    def get_name(self):
        #Gets the player's name.
        return self.name

    def get_rack_str(self):
        #Returns the player's tile-rack.
        return self.rack.get_rack_str()

    def get_rack_arr(self):
        #Returns the player's tile-rack as an array.
        return self.rack.get_rack_arr()
    
    def get_rack_list(self):
        return self.rack.get_rack_list()
        #Returns the player's tile-rack as a list.
    
    def increase_score(self, increase):
        #Increases the player's score by integer 'increase'
        self.score += increase

    def get_score(self):
        #Returns the score of the player.
        return self.score

class Board:
    def __init__(self):
        #Constructor method for the board
        #Creates a 2d array which will act as the Scrabble board, including premium squares.
        self.board = [["   " for i in range(15)] for j in range(15)]
        self.add_premium_squares()
        self.board[7][7] = " * "

    def get_board(self):
        text=""
        #Returns the board as a string.
        board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        boardView=list(self.board)
        board = list(self.board)
        for i in range(len(board)):
            if i < 10:
                board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
            if i >= 10:
                board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        selectBox=0
        
        for event in pygame.event.get():
                # Check for event using pygame functionality every frame.
            if event.type == pygame.QUIT:  #If event is to quit pygame - 
                done = True
                
                        

                    
         
            # Set the screen background
            screen.fill(DGREEN)
            
            # Draw the grid
            for row in range(15):
                for column in range(15):
                    color = CREAM
                    #if board[int(row)][int(column)] == 1:
                        #color = GREEN
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN+ ADDERx,
                                      (MARGIN + HEIGHT) * row + MARGIN + ADDERy,
                                      WIDTH,
                                      HEIGHT])
                    text_surface = my_font2.render(boardView[row][column], False, (0, 0, 0))
                    screen.blit(text_surface, [(MARGIN + WIDTH) * column + MARGIN+ ADDERx,
                                      (MARGIN + HEIGHT) * row + MARGIN+ ADDERy,
                                      WIDTH,
                                      HEIGHT])
                    

         
            #Tick 60 frames per second using pygame, update display.
            clock.tick(60)
            pygame.display.flip()
            pygame.display.update()
                
        return board_str

    def add_premium_squares(self):
        #Sets the premium squares which can adjust the score of the placed word.
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for coordinate in TRIPLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "***"
        #Triple the score of the word.
        for coordinate in TRIPLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "'''"
        #Triple the score of the current tile.
        for coordinate in DOUBLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "**"
        #Double the score of the word.
        for coordinate in DOUBLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "''"
        #Double the score of the current tile.

    def place_word(self, word, location, direction, player):
        #After validation of the word using check_word, this method places the word on the board.
        global premium_spots
        premium_spots = []
        direction = direction.lower()
        word = word.upper()

        #Places the word going right.
        if direction.lower() == "right":
            for i in range(len(word)):
                if self.board[location[0]][location[1]+i] != "   ":
                    premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                self.board[location[0]][location[1]+i] = " " + word[i] + " "

        #Places the word going down.
        elif direction.lower() == "down":
            for i in range(len(word)):
                if self.board[location[0]][location[1]+i] != "   ":
                    premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                self.board[location[0]+i][location[1]] = " " + word[i] + " "

        #Removes tiles from the rack of the current player and replenishes the rack with letters from the bag
        #Ensures 7 letters are in the rack.
                
        for letter in word:
            for tile in player.get_rack_arr():
                if tile.get_letter() == letter:
                    player.rack.remove_from_rack(tile)
        player.rack.replenish_rack()

    def board_array(self):
        #Returns the two-dimensional array of the board.
        return self.board

class Word:
    #Constructor method for the board.
    def __init__(self, word, location, player, direction, board):
        self.word = word.upper()
        self.location = location
        self.player = player
        self.direction = direction.lower()
        self.board = board

    def check_word(self):
        #The code verifies whether the word is in the dictionary "dic.txt"
        # and its location is valid. It manages potential word overlapping.
        global round_number, players
        word_score = 0
        global dictionary 
        if "dictionary" not in globals():
            dictionary = open("dic.txt").read().splitlines()

        current_board_ltr = ""
        needed_tiles = ""
        blank_tile_val = ""


        #If the word is already played, it cannot be played again.
        #if self.word in boardWords:
            #return "Error: invalid."

        #If the word to be played is already played and the previously played word is not a substring of the word, it cannot be played.
        for i in range(0,len(boardWords)-1):
            for j in range(1,len(boardWords[i])-1):
                if self.word in boardWords[i] and boardWords[i] not in self.word:
                    return "Error: invalid." 

        #Assuming that the player is not skipping the turn:
        if self.word != "":

            #Allows for players to declare the value of a blank tile.
            if "#" in self.word:
                while len(blank_tile_val) != 1:
                    blank_tile_val = input("Please enter the letter value of the blank tile: ")
                self.word = self.word[:word.index("#")] + blank_tile_val.upper() + self.word[(word.index("#")+1):]

            #Reads in the board's current values under where the word that is being played will go. Raises an error if the direction is not valid.
            if self.direction == "right":
                #for i in self.board[self.location[1]+1]:

                    #if (i.strip().isupper() or i.strip().islower()):# and i not in tileArr and self.word.split()[i] != self.word.split()[0]:
                        #return "Error: adjacent letters in column"
                #for i in self.board[self.location[1]+1]:

                    #if (i.strip().isupper() or i.strip().islower()) and i not in tileArr and self.word.split()[i] != self.word.split()[0]:
                        #return "Error: adjacent letters in row"
                try:
                    for i in range(len(self.word)):
                        if self.board[self.location[0]][self.location[1]+i][1] == " " or self.board[self.location[0]][self.location[1]+i] == "'''" or self.board[self.location[0]][self.location[1]+i] == "***" or self.board[self.location[0]][self.location[1]+i] == "''" or self.board[self.location[0]][self.location[1]+i] == "**" or self.board[self.location[0]][self.location[1]+i][1] == "*":
                            current_board_ltr += " "
                        else:
                            current_board_ltr += self.board[self.location[0]][self.location[1]+i][1]
                except:
                    return "Error: invalid."

            elif self.direction == "down":
                #for i in self.board[self.location[0]+1]:
                    #if (i.strip().isupper() or i.strip().islower()): #and i not in tileArr and self.word.split()[i] != self.word.split()[0]:
                        #return "Error: adjacent letters in row"
                #for i in self.board[self.location[0]+1]:
                   #if (i.strip().isupper() or i.strip().islower()) and i not in tileArr and self.word.split()[i] != self.word.split()[0]:
                        #return "Error: adjacent letters in column"

                try:
                    for i in range(len(self.word)):

                            
                        if self.board[self.location[0]+i][self.location[1]] == "   " or self.board[self.location[0]+i][self.location[1]] == "'''" or self.board[self.location[0]+i][self.location[1]] == "***" or self.board[self.location[0]+i][self.location[1]] == "''" or self.board[self.location[0]+i][self.location[1]] == "**" or self.board[self.location[0]+i][self.location[1]] == " * ":
                             current_board_ltr += " "
                        else:
                            current_board_ltr += self.board[self.location[0]+i][self.location[1]][1]
                except:
                    return "Error: invalid."


  
            else:
                return "Error: please enter a valid direction."

            #Raises an error if the word being played is not in the official scrabble dictionary (dic.txt).
            if self.word not in dictionary:
                return "Please enter a valid dictionary word.\n"

            #Ensures that the words overlap correctly. If there are conflicting letters between the current board and the word being played, raises an error.
            for i in range(len(self.word)):
                if current_board_ltr[i] == " ":
                    needed_tiles += self.word[i]
                elif current_board_ltr[i] != self.word[i]:
                    print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                    return "The letters do not overlap correctly, please choose another word."

            #If there is a blank tile, remove it's given value from the tiles needed to play the word.
            if blank_tile_val != "":
                needed_tiles = needed_tiles[needed_tiles.index(blank_tile_val):] + needed_tiles[:needed_tiles.index(blank_tile_val)]

            #Ensures that the word will be connected to other words on the playing board.
            if (round_number != 1 or (round_number == 1 and players[0] != self.player)) and current_board_ltr == " " * len(self.word):
                print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                return "Please connect the word to a previously played letter."

            #Raises an error if the player does not have the correct tiles to play the word.
            for letter in needed_tiles:
                if letter not in self.player.get_rack_str() or self.player.get_rack_str().count(letter) < needed_tiles.count(letter):
                    return "You do not have the tiles for this word\n"

            #Raises an error if the location of the word will be out of bounds.
            if self.location[0] > 14 or self.location[1] > 14 or self.location[0] < 0 or self.location[1] < 0 or (self.direction == "down" and (self.location[0]+len(self.word)-1) > 14) or (self.direction == "right" and (self.location[1]+len(self.word)-1) > 14):
                return "Location out of bounds.\n"

            #Ensures that first turn of the game will have the word placed at (7,7).
            if round_number == 1 and players[0] == self.player and self.location != [7,7]:
                return "The first turn must begin at location (7, 7).\n"
            return True

        #If the user IS skipping the turn, confirm. If the user replies with "Y", skip the player's turn. Otherwise, allow the user to enter another word.
        else:
            if True:#input("Are you sure you would like to skip your turn? (y/n)").upper() == "Y":
                if round_number == 1 and players[0] == self.player:
                    return "Please do not skip the first turn. Please enter a word."
                return True
            else:
                return "Please enter a word."

    def calculate_word_score(self):
        #Calculates the score of a word, allowing for the impact by premium squares.
        global LETTER_VALUES, premium_spots
        word_score = 0
        for letter in self.word:
            for spot in premium_spots:
                if letter == spot[0]:
                    if spot[1] == "'''":
                        word_score += LETTER_VALUES[letter] * 2
                    elif spot[1] == "''":
                        word_score += LETTER_VALUES[letter]
            word_score += LETTER_VALUES[letter]
        for spot in premium_spots:
            if spot[1] == "***":
                word_score *= 3
            elif spot[1] == "**":
                word_score *= 2
        self.player.increase_score(word_score)

    def set_word(self, word):
        self.word = word.upper()

    def set_location(self, location):
        self.location = location

    def set_direction(self, direction):
        self.direction = direction

    def get_word(self):
        
        return self.word


def splitIt(word):
    return [char for char in word]
                     










########################### PLAYER TURN BASED ALGORITHM ###########################







def turn(player, board, bag):
    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()
    #Begins a turn, by displaying the current board, getting the information to play a turn, and creates a recursive loop to allow the next person to play.
    global round_number, players, skipped_turns
    #If the number of skipped turns is less than 6 and a row, and there are either tiles in the bag, or no players have run out of tiles, play the turn.
    #Otherwise, end the game.
    if (skipped_turns < 6) or (player.rack.get_rack_length() == 0 and bag.get_remaining_tiles() == 0):

        #Displays whose turn it is, the current board, and the player's rack.
        print("\nRound " + str(round_number) + ": " + player.get_name() + "'s turn \n")
        print(board.get_board())
        print("\n" + player.get_name() + "'s Letter Rack: " + player.get_rack_str())

        text=""
        word_to_play=""
        word=""
        direction=""


        pygame.draw.rect(screen, DGREEN, pygame.Rect(1920 - 200, 1080/2, 200, 200))
        userTurnText = my_font.render(player.get_name()+"'s turn",True,(255,255,0))
        screen.blit(userTurnText, (1920 - 200, 1080/2))

        pygame.draw.rect(screen, DGREEN, pygame.Rect(1920/2 -5, 150, 30, 30))
        textScore1 = my_font.render(str(players[0].get_score())+" - ",True,(0,255,0))
        screen.blit(textScore1, (1920/2 -15, 150))

        pygame.draw.rect(screen, DGREEN, pygame.Rect(725, 7/550, 30, 30))
        textScore2 = my_font.render(str(players[1].get_score()),True,(255,55,32))
        screen.blit(textScore2, (1920/2 +10, 150))
            
        selectBox=1


        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()

########################### USER TURN ###########################


        
        if player.get_name() == "User":
            userTurnText = my_font.render("Type a word.",True,(255,255,0))
            
            screen.blit(userTurnText, (1920/2 -50, 50))
            clock.tick(60)
            pygame.display.update()

            
            while(selectBox==1):
                

                textSurf = my_font.render(text,True,(255,255,255))
                textBox = pygame.Rect(1920/8,1080/2,250,50)
                pygame.draw.rect(screen,(CREAM),textBox,2)
                
                screen.blit(textSurf,(1920/8 + 10 ,1080/2 + 10 , 250,50))
                clock.tick(60)
                pygame.display.update()
                


        
                for event in pygame.event.get():
                    if len(text) > 20:
                        text = ""
                        pygame.draw.rect(screen, DGREEN, pygame.Rect(1920/8, 1080/2, 250, 50))
                        
                        pygame.display.flip()
                        

                        clock.tick(60)
                        pygame.display.update()
                    rack=player.get_rack_str()
                    textRack = my_font2.render(rack,True,BLACK)
                    if event.type == pygame.KEYDOWN:
                        
                        screen.blit(textSurf,(1920/8 + 10,1080/2 + 10,250,50))
                        pygame.display.flip()

                        pygame.draw.rect(screen,GREEN,textBox,2)
                        if selectBox == 1:
                            if event.key == pygame.K_BACKSPACE:
                                text=""
                                pygame.draw.rect(screen, DGREEN, pygame.Rect(1920/8, 1080/2, 250, 50))

                                pygame.display.flip()
                                

                                clock.tick(60)
                                pygame.display.update()
                            if event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                quit()


                                pygame.display.update()


                            else:
                                text += event.unicode
                                #print(text)
                            if event.key == pygame.K_RETURN:  # <-- key instead of type
                                word_to_play=text
                                word_to_play=word_to_play.strip()
                                word_to_play=word_to_play.upper()
                                text=""
                                selectBox=0
                            if event.key == pygame.K_ESCAPE:
                                exit

                            
                    
                    screen.blit(textRack,(1920/2 - 85, 1000))
                    clock.tick(60)
                    pygame.display.flip()
                    pygame.display.update()

            click=False
            pygame.draw.rect(screen, (DGREEN), pygame.Rect(1920/2 - 100, 50, 600, 50))
            userTurnText = my_font.render("Select a tile.",True,(255,255,0))
            screen.blit(userTurnText, (1920/2 - 50, 50))
            clock.tick(60)
            pygame.display.update()
            while(True):
                
                for event in pygame.event.get():
                    print("Click tile")
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print("")
                        pos = pygame.mouse.get_pos()
                        pos = (pos[0]-ADDERx, pos[1]-ADDERy)

                        col1 = (pos[0]) // ((WIDTH + MARGIN))
                        row1 = (pos[1]) // ((HEIGHT + MARGIN))

                        grid[row1][col1] = "1"
                        print("Click ", pos, "Grid coordinates: ", row1, col1)
                        click=True
                        col=str(col1)
                        row=str(row1)
                clock.tick(60)
                pygame.display.flip()
                pygame.display.update()
                if click == True:
                    break

            #col = input("Column number: ")
            #row = input("Row number: ")
            #if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                #location = [-1, -1]
           # else:
            location = [int(row), int(col)]
            click=False
            pygame.draw.rect(screen, (DGREEN), pygame.Rect(1920/2 - 100 , 50, 600, 40))
            userTurnText = my_font.render("Select a direction. (DOWN/RIGHT)",True,(255,255,0))
            screen.blit(userTurnText, (1920/2 - 100 , 50))
            clock.tick(60)
            pygame.display.update()
            while(True):
                for event in pygame.event.get():
                    print("Click tile")
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print("")
                        pos = pygame.mouse.get_pos()

                        if pos[0] < 720:
                            direction="down"
                        if pos[0] > 720:
                            direction="right"
                                
                        
                        click=True
                    clock.tick(60)
                    pygame.display.flip()
                    pygame.display.update()
                if click == True:
                    break



########################### ARTIFICIAL INTELLIGENCE TURN ###########################
                
        if player.get_name() == "AI":
            pygame.draw.rect(screen, (DGREEN), pygame.Rect(1920/2 - 100, 50, 600, 50))
            userTurnText = my_font.render("AI is thinking.",True,(255,255,0))
            screen.blit(userTurnText, (1920/2 - 50, 50))
            clock.tick(60)
            pygame.display.update()
            Z=[]
            accept=False
            for i in range (0,randint(1000,2500)):
                shuffleList=player.get_rack_list()
                shuffleList=shuffleList+tileArr
                random.shuffle(shuffleList)
                sample=random.sample(shuffleList,randint(2,7))
                random.shuffle(sample)
                result = ''.join(sample)
                result=splitIt(result)
                result2 = ''.join(result)
                word_to_play=result2
                word_to_play=word_to_play.strip()
                word_to_play=word_to_play.upper()
                if word_to_play in open("dic.txt").read().splitlines():
                    Z.append(word_to_play)
            Z.sort(key=len)
            Z.reverse()
            checkerAI=False
            counter=0
            for X in Z:
                checkerAI=False
                counter=counter+1
                for row__ in range(1,13):

                    for col__ in range (1,13):

                        for T1 in range(1,2):
                        #if True:

                            #i=randint(1,2)

                            if T1 ==1:
                                directionAI="down"
                            if T1 ==2:
                                directionAI="right"
                            #print(X,col__,row__)
                            wordAI = Word(X, [row__,col__], player, directionAI, board.board_array())
                            checkerAI=wordAI.check_word()
                            if checkerAI == "Error: invalid.":
                                break

                            

                            #print(checkerAI)
                            if checkerAI !=True:
                                    t=1
                                    #print(X)
                                    #print(wordAI.location)
                                    #print(player)
                                    #print(wordAI.direction)
                            else:
                                    print('Valid')
                                    location=[row__,col__]
                                    col=str(col__)
                                    row=str(row__)
                                    direction=directionAI
                                    word_to_play=X
                                    accept=True
                                    print(word_to_play, row, col, direction)
                                    break
                            if counter%500 == 0:
                                print(X,wordAI.location,wordAI.direction,checkerAI)
                        if accept==True:
                            break
                    if accept==True:
                        break
                if accept==True:
                    print(X,wordAI.location,wordAI.direction,checkerAI)
                    print(Z)
                    break
                print(X,wordAI.location,wordAI.direction,checkerAI)
                print(Z)
                            
                                

                                                            
            
            clock.tick(60)
            pygame.display.flip()
            pygame.display.update()

                

            
        print(word_to_play, row, col, direction)
        word = Word(word_to_play, location, player, direction, board.board_array())
        #print('done')
        #turn(player,board,bag)
        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()
        print(board.board_array())
        checker=word.check_word()
        #If the first word throws an error, creates a recursive loop until the information is given correctly.
        #print('checking')
        if checker !=True:
            print(checker)
            print(word_to_play)
            print(location)
            print(player)
            print(word.direction)
            turn(player, board, bag)
        else:
            print('Valid')

            
            

            
            #word.set_word(word_to_play)
            #location = []
            #col = input("Column number: ")
            #row = input("Row number: ")
            if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                location = [-1, -1]
            else:
                word.set_location([int(row), int(col)])
                location = [int(row), int(col)]
            #screen.fill(BLACK)
         
            #board.get_board()

         
            # Limit to 60 frames per second
            clock.tick(60)
            pygame.display.flip()
            pygame.display.update()
        #If the user has confirmed that they would like to skip their turn, skip it.
        #Otherwise, plays the correct word and prints the board.
        if word.get_word() == "":
            print("Your turn has been skipped.")
            skipped_turns += 1
        else:
            board.place_word(word_to_play, location, direction, player)
            colArr.append(col)
            rowArr.append(row)
            for letter in word_to_play:
                tileArr.append(letter)
            boardWords.append(word_to_play)
            word.calculate_word_score()
            skipped_turns = 0
            clock.tick(60)
            pygame.display.flip()
            pygame.display.update()

        #Prints the current player's score
        print("\n" + player.get_name() + "'s score is: " + str(player.get_score()))

        #Gets the next player.
        if players.index(player) != (len(players)-1):
            player = players[players.index(player)+1]
        else:
            player = players[0]
            round_number += 1

        #Recursively calls the function in order to play the next turn.
        word=""
        word_to_play=""
        turn(player, board, bag)

    #If the number of skipped turns is over 6 or the bag has both run out of tiles and a player is out of tiles, end the game.
    else:
        end_game()

def start_game():
    #Begins the game and calls the turn function.
    global round_number, players, skipped_turns
    board = Board()
    bag = Bag()

    #Asks the player for the number of players.
    num_of_players = 2

    #Welcomes players to the game and allows players to choose their name.
    players = []
    players.append(Player(bag))
    players[0].set_name("User")
    players.append(Player(bag))
    players[1].set_name("AI")

    #Sets the default value of global variables.
    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game():
    #Forces the game to end when the bag runs out of tiles.
    global players
    highest_score = 0
    winning_player = ""
    for player in players:
        if player.get_score > highest_score:
            highest_score = player.get_score()
            winning_player = player.get_name()
    print("The game is over! " + winning_player + ", you have won!")

    if input("\nWould you like to play again? (y/n)").upper() == "Y":
        start_game()

start_game()