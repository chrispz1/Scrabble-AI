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
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
 
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

        #If the input does not contain a value to skip a turn: 
        if self.word != "":
            

            if self.direction == "right":
                #Further validation of the word, using try statement to handle potential errors of the attempted word.
                #Validation for attempted "right" and "down" placement respectively.
                try:
                    for i in range(len(self.word)):
                        if self.board[self.location[0]][self.location[1]+i][1] == " " or self.board[self.location[0]][self.location[1]+i] == "'''" or self.board[self.location[0]][self.location[1]+i] == "***" or self.board[self.location[0]][self.location[1]+i] == "''" or self.board[self.location[0]][self.location[1]+i] == "**" or self.board[self.location[0]][self.location[1]+i][1] == "*":
                            current_board_ltr += " "
                        else:
                            current_board_ltr += self.board[self.location[0]][self.location[1]+i][1]
                except:
                    return "Error: invalid."

            elif self.direction == "down":

                try:
                    for i in range(len(self.word)):

                            
                        if self.board[self.location[0]+i][self.location[1]] == "   " or self.board[self.location[0]+i][self.location[1]] == "'''" or self.board[self.location[0]+i][self.location[1]] == "***" or self.board[self.location[0]+i][self.location[1]] == "''" or self.board[self.location[0]+i][self.location[1]] == "**" or self.board[self.location[0]+i][self.location[1]] == " * ":
                             current_board_ltr += " "
                        else:
                            current_board_ltr += self.board[self.location[0]+i][self.location[1]][1]
                except:
                    return "Error: invalid."

            else:
                #Returns an error code if the attempted word does not have a valid direction.
                return "Error: please enter a valid direction."

            
            if self.word not in dictionary:
                #Returns an error code if the attempted word is not in the dictionary.
                return "Please enter a valid dictionary word.\n"

            #Ensures the validation of overlapping words, according to the rules of Scrabble.
            for i in range(len(self.word)):
                if current_board_ltr[i] == " ":
                    needed_tiles += self.word[i]
                elif current_board_ltr[i] != self.word[i]:
                    print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                    return "The letters do not overlap correctly, please choose another word."


            #Ensures the connection of the word to be placed with the currently placed words on the board, according to the rules of Scrabble.
            if (round_number != 1 or (round_number == 1 and players[0] != self.player)) and current_board_ltr == " " * len(self.word):
                print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + self.word + ", Needed_Tiles: " + needed_tiles)
                return "Please connect the word to a previously played letter."

            #Returns an error if the current player does not have the correct tiles for the word.
            for letter in needed_tiles:
                if letter not in self.player.get_rack_str() or self.player.get_rack_str().count(letter) < needed_tiles.count(letter):
                    return "You do not have the tiles for this word\n"

            #Returns an error if the location is not wiithin the board.
            if self.location[0] > 14 or self.location[1] > 14 or self.location[0] < 0 or self.location[1] < 0 or (self.direction == "down" and (self.location[0]+len(self.word)-1) > 14) or (self.direction == "right" and (self.location[1]+len(self.word)-1) > 14):
                return "Location out of bounds.\n"

            #Ensures that the first turn can only be played from the centre of the board, 7, 7
            if round_number == 1 and players[0] == self.player and self.location != [7,7]:
                return "The first turn must begin at location (7, 7).\n"
            return True

        #Ensures that first turn cannot be skipped.
        else:
            if True:
                if round_number == 1 and players[0] == self.player:
                    return "Please do not skip the first turn. Please enter a word."
                return True
            else:
                return "Please enter a word."

    def calculate_word_score(self):
        #Calculates the score of the word, accounting for premium squares.
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
        #Method to force set of a word class instance.

    def set_location(self, location):
        self.location = location
        #Method to force location of a word class instance.

    def set_direction(self, direction):
        self.direction = direction
        #Method to force set direction of word class instance.

    def get_word(self):
        #Gets word class instance.
        
        return self.word




def splitIt(word):
    #Defines splitIt function which returns a list of the characters within a word for the AI to handle word generation.
    return [char for char in word]
                     



########################### PLAYER TURN BASED ALGORITHM ###########################






#Turn function: plays for each turn, switching between players.
def turn(player, board, bag):
    
    #Updates screen.
    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()
    
    #Begins the turn, displays board on screen and starts the start of the game.
    #Creates a recursive loop by calling this method for each player to play (Including AI)
    
    global round_number, players, skipped_turns

    if (skipped_turns < 6) or (player.rack.get_rack_length() == 0 and bag.get_remaining_tiles() == 0):

        #Console operations to print current status of game.
        print("\nRound " + str(round_number) + ": " + player.get_name() + "'s turn \n")
        print(board.get_board())
        print("\n" + player.get_name() + "'s Letter Rack: " + player.get_rack_str())

        #Initialises required variables for User(s) / AI play.
        text=""
        word_to_play=""
        word=""
        direction=""


        ### Displays turns on screen.
        pygame.draw.rect(screen, DGREEN, pygame.Rect(1920 - 200, 1080/2, 200, 200))
        userTurnText = my_font.render(player.get_name()+"'s turn",True,(255,255,0))
        screen.blit(userTurnText, (1920 - 200, 1080/2))

        pygame.draw.rect(screen, DGREEN, pygame.Rect(1920/2 -5, 150, 30, 30))
        textScore1 = my_font.render(str(players[0].get_score())+" - ",True,(0,255,0))
        screen.blit(textScore1, (1920/2 -15, 150))

        pygame.draw.rect(screen, DGREEN, pygame.Rect(725, 7/550, 30, 30))
        textScore2 = my_font.render(str(players[1].get_score()),True,(255,55,32))
        screen.blit(textScore2, (1920/2 +10, 150))
        ###

        #Variable to manage if user text-input box is accessible.
        selectBox=1

        #Updates screen.
        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()

########################### USER TURN ###########################


        #Such that the turn is the user's, prompt to type a word on screen.
        if player.get_name() == "User":
            userTurnText = my_font.render("Type a word.",True,(255,255,0))
            
            screen.blit(userTurnText, (1920/2 -50, 50))
            clock.tick(60)
            pygame.display.update()


            #Such that the text-box is activated.
            while(selectBox==1):
                

                #Display the textbox.
                textSurf = my_font.render(text,True,(255,255,255))
                textBox = pygame.Rect(1920/8,1080/2,250,50)
                pygame.draw.rect(screen,(CREAM),textBox,2)
                
                screen.blit(textSurf,(1920/8 + 10 ,1080/2 + 10 , 250,50))
                clock.tick(60)
                pygame.display.update()
                


                #Loop to detect player input and actions.
                for event in pygame.event.get():
                    #Such that the length of the text-box input 'text' is no greater that 20 characters.
                    #In the case that this is true, reset the text box.
                    if len(text) > 20:
                        text = ""
                        pygame.draw.rect(screen, DGREEN, pygame.Rect(1920/8, 1080/2, 250, 50))

                        #Update screen.
                        pygame.display.flip()
                        clock.tick(60)
                        pygame.display.update()



                    #Get the rack of the player and render it to the screen.
                    rack=player.get_rack_str()
                    textRack = my_font2.render(rack,True,BLACK)

                    #Handles key presses to display to the textbox.
                    
                    if event.type == pygame.KEYDOWN:
                        
                        screen.blit(textSurf,(1920/8 + 10,1080/2 + 10,250,50))
                        pygame.display.flip()

                        pygame.draw.rect(screen,GREEN,textBox,2)
                        if selectBox == 1:
                            if event.key == pygame.K_BACKSPACE:
                                text=""
                                pygame.draw.rect(screen, DGREEN, pygame.Rect(1920/8, 1080/2, 250, 50))

                                #Update the screen.
                                pygame.display.flip()
                                clock.tick(60)
                                pygame.display.update()


                            #Quit if backspace is pressed.
                            elif event.key == pygame.K_ESCAPE:
                                
                                pygame.quit()
                                quit()


                                #Update display.
                                pygame.display.update()


                            else:
                                text += event.unicode

                               
                            if event.key == pygame.K_RETURN:
                                word_to_play=text
                                word_to_play=word_to_play.strip()
                                word_to_play=word_to_play.upper()
                                text=""
                                selectBox=0
                            #If enter is pressed on the textbox, initialises that this is the 'word_to_play', in variable form which is stripped of spaces ...
                            #... and made upper-case.
                            #Textbox text set to default state and text-box de-activated.

                            
                    #Display the textrack and update the screen
                    screen.blit(textRack,(1920/2 - 85, 960))
                    clock.tick(60)
                    pygame.display.flip()
                    pygame.display.update()

            
            #This portion of code serves to handle the clicks of the player once the word is entered.
            #The user must click a tile to place their chosen word.

            click=False
            pygame.draw.rect(screen, (DGREEN), pygame.Rect(1920/2 - 100, 50, 600, 50))
            userTurnText = my_font.render("Select a tile.",True,(255,255,0))
            screen.blit(userTurnText, (1920/2 - 50, 50))
            clock.tick(60)
            pygame.display.update()


            #Loops until a click is detected.
            while(True):
                
                for event in pygame.event.get():
                    print("Click tile")
                    #Using pygames mouse-down detection to gather the x/y co-ordinates of the click ...
                    #... and translate it to the 2d array 'grid' representing the 'col' and 'row' location
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

            #If the click has been registered, the column and row integers are translated to string variables ...
            #... and the location is set for the word.

            location = [int(row), int(col)]
            click=False



            #This portion of code serves to handle the direction of choice for the player once the word is entered.
            #The user must click a tile to place their chosen word.
            pygame.draw.rect(screen, (DGREEN), pygame.Rect(1920/2 - 100 , 50, 600, 40))
            userTurnText = my_font.render("Select a direction. (Click the right side of the screen for RIGHT or the left side of the screen for DOWN)",True,(255,255,0))
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
                    #Using pygames mouse-down detection to gather the x/y co-ordinates of the click ...
                    #... If the user clicks the right side of the screen, RIGHT is passed as the direction, or the left side of the screen for DOWN.
                        click=True
                    clock.tick(60)
                    pygame.display.flip()
                    pygame.display.update()
                if click == True:
                    break



########################### ARTIFICIAL INTELLIGENCE TURN ###########################


        #AI's turn       
        if player.get_name() == "AI":
            #Displays that the AI is thinking as there is a delay when it searches for potential words.
            pygame.draw.rect(screen, (DGREEN), pygame.Rect(1920/2 - 100, 50, 600, 50))
            userTurnText = my_font.render("AI is thinking.",True,(255,255,0))
            screen.blit(userTurnText, (1920/2 - 50, 50))
            clock.tick(60)
            pygame.display.update()

            
            Z=[]
            #Z: array to hold valid dictionary words it creates when trying different combinations to potentially place on the board.
            accept=False
            #Variable to determine is a valid word is found.

            #1. Shuffles its words, and words on the board using shuffleList and tileArr (which holds the current letters on the board).
            #2. Takes a sample of this (between 2 and 7 characters long)
            #3. Formats this word.
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
            #4. Checks if the word is within the dictionary.
                if word_to_play in open("dic.txt").read().splitlines():
                    Z.append(word_to_play)
            #5. ... If so, append it to Z.


            Z.sort(key=len)
            Z.reverse()
            
            #Sort Z (the potential words to play) in length order, from longest to shortest.


            #This portion of the code serves to check each potential word, (for X in Z), for its validity to be played.
            checkerAI=False
            counter=0

            #Nested for loops serve to check each location on the board, using row__ and col__, to see which of the potential words can be played.
            #For each location, it is tried downwards and rightwards.
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


                                
                            wordAI = Word(X, [row__,col__], player, directionAI, board.board_array())
                            checkerAI=wordAI.check_word()
                            if checkerAI == "Error: invalid.":
                                break
                            #Instantiates a Word class as wordAI, with required parameters.
                            #From here, checkerAI uses the check_word function on the word to see if its valid.
                            #If it is invalid, break from this loop.

                            

    
                            if checkerAI !=True:
                                    t=1
                                    #Do nothing if checkerAI returns an error.
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
                                #If checkerAI returns true, the word is valid ...
                                #... set the required variables for word class instantiation including col, row, direction and word_to_play
                                #set accept to True and break the loops.
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
                            
                                

                                                            
            #Update display.
            clock.tick(60)
            pygame.display.flip()
            pygame.display.update()

                
################################MAIN CODE FOR TURN###############################
            
        print(word_to_play, row, col, direction)
        #Instantiate a new word class instance object as the word to play, with given set parameters, for the current user turn (including AI)
        word = Word(word_to_play, location, player, direction, board.board_array())
        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()
        print(board.board_array())

        #Utilises the word instance's check_word method to finally validate the word.
        checker=word.check_word()
        if checker !=True:
            print(checker)
            print(word_to_play)
            print(location)
            print(player)
            print(word.direction)
            turn(player, board, bag)
        else:
            print('Valid')

            #Initalises the placement of the word.
            if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                location = [-1, -1]
            else:
                word.set_location([int(row), int(col)])
                location = [int(row), int(col)]


         
            #Update screen
            clock.tick(60)
            pygame.display.flip()
            pygame.display.update()
            
        #If the word string has been entered, or set, as nothing, the turn is skipped,
        #... otherwise, the word is placed using the board class's place_word method,
        #... required variables are updated and the score is calculated.
            
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

        #Gets the next player, setting up for the next turn.
        #If all players have played, the next round is played.
        
        if players.index(player) != (len(players)-1):
            player = players[players.index(player)+1]
        else:
            player = players[0]
            round_number += 1

        #Recursively calls the turn function to act as the game loop.
        word=""
        word_to_play=""
        turn(player, board, bag)

    #Ends the game if the bag has run out of tiles and the player's have run out of tiles.
    else:
        end_game()

def start_game():
    #Starts the game and instantiates the board and bag objects.
    
    global round_number, players, skipped_turns
    board = Board()
    bag = Bag()

    #Number of players setting.
    num_of_players = 2

    #Adds the players to the game and passes the bag as an argument to all players.
    players = []
    players.append(Player(bag))
    players[0].set_name("User")
    players.append(Player(bag))
    players[1].set_name("AI")

    #Initialises global variables.
    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game():
    #Ends the game when the bag runs out of tiles.
    global players
    highest_score = 0
    winning_player = ""
    #Gets name of player with highest score and displays it to the screen.
    for player in players:
        if player.get_score > highest_score:
            highest_score = player.get_score()
            winning_player = player.get_name()
    while(True):
        screen.fill(DGREEN)
        endGameText=("The game is over! " + winning_player + ", has won!")
        userTurnText = my_font.render(endGameText,True,(255,255,0))
        screen.blit(userTurnText, (1920/2 - 50, 500))
        clock.tick(60)
        pygame.display.update()

#Starts game
start_game()
