import pygame as pyg
import os
import random

# Declare all variables
# Create a dictionary to store all the images files
tileList = {"A": 'tiles/A.png',
            "B": 'tiles/B.png',
            "C": 'tiles/C.png',
            "D": 'tiles/D.png',
            "E": 'tiles/E.png',
            "F": 'tiles/F.png',
            "G": 'tiles/G.png',
            "H": 'tiles/H.png',
            "I": 'tiles/I.png',
            "J": 'tiles/J.png',
            "K": 'tiles/K.png',
            "L": 'tiles/L.png',
            "M": 'tiles/M.png',
            "N": 'tiles/N.png',
            "O": 'tiles/O.png',
            "P": 'tiles/P.png',
            "Q": 'tiles/Q.png',
            "R": 'tiles/R.png',
            "S": 'tiles/S.png',
            "T": 'tiles/T.png',
            "U": 'tiles/U.png',
            "V": 'tiles/V.png',
            "W": 'tiles/W.png',
            "X": 'tiles/X.png',
            "Y": 'tiles/Y.png',
            "Z": 'tiles/Z.png',
            "NA": 'tiles/empty.png',
            'white': 'tiles/white.png'}

# Dictionary with keys:letters, and values:scores

tileScore = {"A": 1,
             "B": 3,
             "C": 3,
             "D": 1,
             "E": 1,
             "F": 4,
             "G": 2,
             "H": 4,
             "I": 1,
             "J": 8,
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
             "Z": 10}


blue_color = (0, 0, 255)
green_color = (0, 255, 0)
red_color = (255, 0, 0)
orange_color = (255, 128, 0)
black_color = (0, 0, 0)
white_color = (255, 255, 255)

global screen
global basicfont
# tempTile = 0

# Create classes
# Create class Player
class Player:

    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.score = 0


# Create 2 to 4 player instances
Player1 = Player('Player 1')
Player2 = Player('Player 2')


# Create class Tile
class Tile:

    def __init__(self, name, score, image, modifier):
        self.name = name
        self.score = score
        self.image = image
        self.modifier = modifier


# Create all the Tile instances, there is a total of 96 instances
# A
A_tile1 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile2 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile3 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile4 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile5 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile6 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile7 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile8 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
A_tile9 = Tile('A', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['A'])), (30, 30)), 'None')
# B
B_tile1 = Tile('B', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['B'])), (30, 30)), 'None')
B_tile2 = Tile('B', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['B'])), (30, 30)), 'None')
# C
C_tile1 = Tile('C', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['C'])), (30, 30)), 'None')
C_tile2 = Tile('C', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['C'])), (30, 30)), 'None')
# D
D_tile1 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
D_tile2 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
D_tile3 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
D_tile4 = Tile('D', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['D'])), (30, 30)), 'None')
# E
E_tile1 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile2 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile3 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile4 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile5 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile6 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile7 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile8 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile9 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile10 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile11 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
E_tile12 = Tile('E', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['E'])), (30, 30)), 'None')
# F
F_tile1 = Tile('F', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['F'])), (30, 30)), 'None')
F_tile2 = Tile('F', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['F'])), (30, 30)), 'None')
# G
G_tile1 = Tile('G', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
G_tile2 = Tile('G', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
G_tile3 = Tile('G', 2, pyg.transform.scale(pyg.image.load(os.path.join(tileList['G'])), (30, 30)), 'None')
# H
H_tile1 = Tile('H', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['H'])), (30, 30)), 'None')
H_tile2 = Tile('H', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['H'])), (30, 30)), 'None')
# I
I_tile1 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile2 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile3 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile4 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile5 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile6 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile7 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile8 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
I_tile9 = Tile('I', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['I'])), (30, 30)), 'None')
# J
J_tile1 = Tile('J', 8, pyg.transform.scale(pyg.image.load(os.path.join(tileList['J'])), (30, 30)), 'None')
# K
K_tile1 = Tile('K', 5, pyg.transform.scale(pyg.image.load(os.path.join(tileList['K'])), (30, 30)), 'None')
# L
L_tile1 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile2 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile3 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
L_tile4 = Tile('L', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['L'])), (30, 30)), 'None')
# M
M_tile1 = Tile('M', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['M'])), (30, 30)), 'None')
M_tile2 = Tile('M', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['M'])), (30, 30)), 'None')
# N
N_tile1 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile2 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile3 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile4 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile5 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
N_tile6 = Tile('N', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['N'])), (30, 30)), 'None')
# O
O_tile1 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile2 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile3 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile4 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile5 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile6 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile7 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
O_tile8 = Tile('O', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['O'])), (30, 30)), 'None')
# P
P_tile1 = Tile('P', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['P'])), (30, 30)), 'None')
P_tile2 = Tile('P', 3, pyg.transform.scale(pyg.image.load(os.path.join(tileList['P'])), (30, 30)), 'None')
# Q
Q_tile1 = Tile('Q', 10, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Q'])), (30, 30)), 'None')
# R
R_tile1 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile2 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile3 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile4 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile5 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
R_tile6 = Tile('R', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['R'])), (30, 30)), 'None')
# S
S_tile1 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
S_tile2 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
S_tile3 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
S_tile4 = Tile('S', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['S'])), (30, 30)), 'None')
# T
T_tile1 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile2 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile3 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile4 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile5 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
T_tile6 = Tile('T', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['T'])), (30, 30)), 'None')
# U
U_tile1 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
U_tile2 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
U_tile3 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
U_tile4 = Tile('U', 1, pyg.transform.scale(pyg.image.load(os.path.join(tileList['U'])), (30, 30)), 'None')
# V
V_tile1 = Tile('V', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['V'])), (30, 30)), 'None')
# W
W_tile1 = Tile('W', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['W'])), (30, 30)), 'None')
# X
X_tile1 = Tile('X', 8, pyg.transform.scale(pyg.image.load(os.path.join(tileList['X'])), (30, 30)), 'None')
# Y
Y_tile1 = Tile('Y', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Y'])), (30, 30)), 'None')
Y_tile2 = Tile('Y', 4, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Y'])), (30, 30)), 'None')
# Z
Z_tile1 = Tile('Z', 10, pyg.transform.scale(pyg.image.load(os.path.join(tileList['Z'])), (30, 30)), 'None')
# Empty
# empty = Tile('NA',0, pyg.transform.scale(pyg.image.load(os.path.join(tileList['NA'])), (30, 30)), 'None')
white = Tile('NA', 0, pyg.transform.scale(pyg.image.load(os.path.join(tileList['white'])), (30, 30)), 'None')
# Put them all into a list
allTiles = [A_tile1, A_tile2, A_tile3, A_tile4, A_tile5, A_tile6, A_tile7, A_tile8, A_tile9,
            B_tile1, B_tile2, C_tile1, C_tile2, D_tile1, D_tile2, D_tile3, D_tile4,
            E_tile1, E_tile2, E_tile3, E_tile4, E_tile5, E_tile6, E_tile7, E_tile8, E_tile9, E_tile10, E_tile11,
            E_tile12,
            F_tile1, F_tile2, G_tile1, G_tile2, G_tile3, H_tile1, H_tile2,
            I_tile1, I_tile2, I_tile3, I_tile4, I_tile5, I_tile6, I_tile7, I_tile8, I_tile9,
            J_tile1, K_tile1, L_tile1, L_tile2, L_tile3, L_tile4, M_tile1, M_tile2,
            N_tile1, N_tile2, N_tile3, N_tile4, N_tile5, N_tile6,
            O_tile1, O_tile2, O_tile3, O_tile4, O_tile5, O_tile6, O_tile7, O_tile8,
            P_tile1, P_tile2, Q_tile1, R_tile1, R_tile2, R_tile3, R_tile4, R_tile5, R_tile6,
            S_tile1, S_tile2, S_tile3, S_tile4, T_tile1, T_tile2, T_tile3, T_tile4, T_tile5, T_tile6,
            U_tile1, U_tile2, U_tile3, U_tile4, V_tile1, W_tile1, X_tile1, Y_tile1, Y_tile2, Z_tile1]

# Create a 15 * 15 grid
board_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Use random to randomly select tiles
tileBank = random.sample(allTiles, len(allTiles))

# Use a global player instance, just to make it easier
playerInstance = Player1


def selectTile(player):
    """Return a list of 7 tiles added together with a given player object"""
    player.tiles.append(tileBank.pop())
    # player.tiles = [U_tile1,U_tile1,U_tile1,U_tile1,U_tile1,U_tile1,white] # test code
    return player.tiles


for i in range(7):
    selectTile(Player1)
    selectTile(Player2)

print('Player 1 tiles: ' + str(Player1.tiles[0].name) + ', ' + str(Player1.tiles[1].name) + ', ' + str(
   Player1.tiles[2].name) + ', ' + (Player1.tiles[3].name) + ', '
     + (Player1.tiles[4].name) + ', ' + (Player1.tiles[5].name) + ', ' + (Player1.tiles[6].name))  # Test code

print('Player 2 tiles: ' + str(Player2.tiles[0].name) + ', ' + str(Player2.tiles[1].name) + ', ' + str(
    Player2.tiles[2].name) + ', ' + (Player2.tiles[3].name) + ', '
      + (Player2.tiles[4].name) + ', ' + (Player2.tiles[5].name) + ', ' + (Player2.tiles[6].name))  # Test code



# Create functions
# Create functions for all calculations
tempTile = 0


def mouseCheck(mouse):
    """This function modify the board with a given mouse coordinate (x,y)
        if the mouse coordinate is between (41,31) and (560,569), it will place a tile on the associated coord of the board
        if the mouse coordinate is between (21,626) and (428,675), it will detect the associated tiles on the player bar, and store it in a variable,
        and delete it from the original player bar list
    """
    # declare variables
    boardX1 = 41
    boardY1 = 31
    boardX2 = 560
    boardY2 = 569
    playerBarX1 = 21
    playerBarX2 = 428
    playerBarY1 = 626
    playerBarY2 = 675
    buttonX1 = 447
    buttonY1 = 624
    buttonX2 = 578
    buttonY2 = 677
    global tempTile
    if mouse[0] >= boardX1 and mouse[0] <= boardX2 and mouse[1] >= boardY1 and mouse[1] <= boardY2:
        x = int(mouse[0] // 40)
        y = int(mouse[1] // 40)
        board_list[y][x] = tempTile
        tempTile = 0
        # print(tempTile.name) # test code
        # pyg.display.flip()
        # print("board") # test code
    elif mouse[0] >= playerBarX1 and mouse[0] <= playerBarX2 and mouse[1] >= playerBarY1 and mouse[1] <= playerBarY2:
        x = int(mouse[0] // 60)
        y = int(mouse[1] // 60)
        tempTile = playerInstance.tiles[x]
        # print(tempTile.name) # test code
        playerInstance.tiles[x] = white
        selectTile(playerInstance)
        # pyg.display.update()
        # print("playerBar") # test code
        # pass
    elif mouse[0] >= buttonX1 and mouse[0] <= buttonX2 and mouse[1] >= buttonY1 and mouse[1] <= buttonY2:
        print("button clicked") # test code
        donebuttonClicked()
        modifyScore(playerInstance)
        print(playerInstance.name) # test codeonebuttonClicked


def donebuttonClicked():
    global tileBank, allTiles, playerInstance, screen
    # tileBank = []
    # tileBank = random.sample(allTiles, len(allTiles))
    playerInstance.tiles = [i for i in playerInstance.tiles if i.name != 'NA']
    if len(tileBank) < 1:
        winner = checkWin()
        screen.blit(basicfont.render('Game Over! Winner: ' + winner + '!', True, (0, 0, 0), (250, 250, 250)), (630, 670))
    # selectTile(playerInstance)
    # pyg.display.update()
    modifyScore(playerInstance)
    if playerInstance == Player1:
        screen.blit(basicfont.render('Player 1 Score: ' + str(playerInstance.score), True, (0, 0, 0), (250, 250, 250)), (630, 610))
        screen.blit(basicfont.render('Tiles Left: ' + str(len(tileBank)), True, (0, 0, 0), (250, 250, 250)), (630, 670))
        playerInstance = Player2
    else:
        screen.blit(basicfont.render('Player 2 Score: ' + str(playerInstance.score), True, (0, 0, 0), (250, 250, 250)),(630, 640))
        screen.blit(basicfont.render('Tiles Left: ' + str(len(tileBank)), True, (0, 0, 0), (250, 250, 250)), (630, 670))
        playerInstance = Player1
    # print(playerInstance.score) # test code
    # pyg.display.update()

def checkWin():
    """Analyze the scores of the players and check win, return player1 or player2 as a string"""
    if player1.score < player2.score:
        return "player 2"
    else:
        return "player 1"


def checkColumn(column):
    """Scan all words that is bigger than length 1 and return a list
        contains all those words"""
    words = []
    one_word = ''
    for i in range(15):
        if board_list[i][column] != 0:
            one_word += board_list[i][column].name
        else:
            words.append(one_word)
            one_word = ''
    words.append(one_word)
    words = [x for x in words if len(x) > 1]
    return words


def checkRow(row):
    """Scan all words in a row that is bigger than length 1 and return a list
        contains all those words"""
    words = []
    one_word = ''
    for i in range(15):
        if board_list[row][i] != 0:
            one_word += board_list[row][i].name
        else:
            words.append(one_word)
            one_word = ''
    words.append(one_word)
    words = [x for x in words if len(x) > 1]
    return words


def checkDict(word):
    '''Checks if word in dictionary'''
    if word in open('dict.txt').read().split():
        return True
    else:
        return False


def listAllTrueWords():
    '''Returns a list of all of the true words on the board'''
    summation = []
    for i in range(15):
        summation.extend(checkRow(i))
        summation.extend(checkColumn(i))
    summation = [x for x in summation if len(x) > 0]
    return [i for i in summation if checkDict(i)]


def totalBoardScore():
    '''Returns total score of all true words on the board'''
    words = ''.join(listAllTrueWords())
    score = 0
    for i in range(len(words)):
        score += tileScore[words[i]]
    return score


old_score = 0
new_score = 0


def modifyScore(player):
    '''Modifies player score, valid words only, invalid=0 points'''
    global old_score
    global new_score
    new_score = totalBoardScore()
    player.score += new_score - old_score
    old_score = new_score


# Pygame main function
def main():
    # initialize pygame
    global screen, basicfont
    pyg.init()
    screen = pyg.display.set_mode((800, 700))
    screen.fill((255, 255, 255))
    pyg.display.set_caption('Scrabble Multiplayer')
    # Display screen
    scrabble_board = pyg.transform.scale(pyg.image.load(os.path.join('scrabble_board_800px.png')), (600, 600))
    screen.blit(scrabble_board, (0, 0))

    # Draw boxes
    pyg.draw.rect(screen, blue_color, (0, 600, 600, 100), 5)
    pyg.draw.rect(screen, green_color, (600, 0, 200, 600), 5)
    for i in range(7):
        pyg.draw.rect(screen, red_color, (20 + 60 * i, 625, 50, 50), 2)

    # draw button
    pyg.draw.rect(screen, green_color, (448, 625, 131, 53), 0)

    # Displaying Player scores and Tiles Remaining
    basicfont = pyg.font.SysFont(None, 25)
    button_text = basicfont.render('End Turn', True, (0, 0, 0), green_color)
    screen.blit(basicfont.render('Player 1 Score: ' + str(Player1.score), True, (0, 0, 0), (250, 250, 250)), (630, 610))
    screen.blit(basicfont.render('Player 2 Score: ' + str(Player2.score), True, (0, 0, 0), (250, 250, 250)),(630, 640))
    screen.blit(basicfont.render('Tiles Left: ' + str(len(tileBank)), True, (0, 0, 0), (250, 250, 250)), (630, 670))
    # tiles_remaining_text = basicfont.render('Tiles Left: ' + '0', True, (0, 0, 0), (250, 250, 250))
    # screen.blit(p1_score_text, (630, 610))
    # screen.blit(p2_score_text, (630, 640))
    screen.blit(button_text, (478, 645))

    # Place tiles in squares

    def showTiles(player):
        for i in range(7):
            screen.blit(player.tiles[i].image, (30 + 60 * i, 635))

    showTiles(playerInstance)

    # Draw the grid
    def drawGrid():
        for i in range(15):
            for j in range(15):
                # tiles_On_Board = pyg.transform.scale(pyg.image.load(os.path.join(tileList['F']))
                # screen.blit(A_tile1.image, (40 + j*35, 43 + i*35))
                if board_list[i][j] != 0:
                    screen.blit(board_list[i][j].image, (40 + j * 35, 41 + i * 35))

    drawGrid()

    # Update the screen to make the changes visible
    pyg.display.update()

    # print('Player 1 tiles: ' + str(Player1.tiles[0].name) + ', ' + str(Player1.tiles[1].name))  # Test code
    # print('Player 2 tiles: ' + str(Player2.tiles[0].name) + ', ' + str(Player2.tiles[1].name))  # Test code

    # print(Player1.tiles[:]) # Test code
    # print(Player2.tiles[:]) # Test code

    # Coordinates
    # Middle: (285, 285)
    # Columns A-O: (43, 77, 112, 147, 181, 216, 250, 285, 319, 354, 388, 424, 458, 493, 528)
    # Rows 1-15: (33, 69, 105, 141, 177, 213, 249, 285, 321, 357, 393, 429, 465, 501, 538)
    # event.button:
    #   1.left click
    #   2.middle click
    #   3.right click
    #   4.scroll up
    #   5.scroll down

    # define a variable to control the main loop
    running = True
    # Attention: These should be included in main()
    # Code to detect mouse click
    while running:
        for event in pyg.event.get():
            if event.type == pyg.MOUSEMOTION:
                mouse = pyg.mouse.get_pos()
                # print(mouse) # test code
            elif event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pyg.mouse.get_pos()
                print(mouse)  # e test code
                mouseCheck(mouse)
                print([i.name for i in playerInstance.tiles])  # test code
                showTiles(playerInstance)
                drawGrid()
                pyg.display.update()
                # print(board_list) # test code
                # print(event.button) # test code
                # print("action performed") # test code
            elif event.type == pyg.QUIT:
                running = False


# pyg.display.update()


if __name__ == "__main__":
    main()
