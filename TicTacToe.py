################## HEADER ################
#Code written by Anne-Lise Marais
#Contact at maraisannelise98 [at] gmail [dot] com

#Run the last script to play Tic Tac Toe with CPU
#Run the two players script to play Tic Tac Toe with someone (not finished)

#requires !pip install inquirer

################### TIC TAC TOE ###########################

#################### FIRST TRY ############################
	



import numpy as np 
import inquirer 
import random 
import time

TTT = np.zeros((3,3)) #Create a matrix of 3 empty rows and columns --> for numbers

Players = ['Player', 'CPU']
Player = random.choice(Players)

#Set possible places

position = ['Top left', 'Top middle', 'Top right', 'Middle left', 'Middle', 'Middle right', 'Bottom left', 'Bottom middle', 'Bottom right'] #Write all possible places

Player_score = 0

def TicTacToePlayer():
	print('Player is you, choose where to place your pawn')
	global Player
	Player = 'Player'
	#Ask question
	questions = [ #open inquirer
  inquirer.List('pawn', #name of whats inquired
                message="Where do you want to place your pawn?", #ask your question
                choices=position, #choices are the positions
            ),
	]
	answer = inquirer.prompt(questions) #make the choice
	print(answer["pawn"]) #print the choice

	#Process the answer

	position.remove(answer['pawn'])#Remove the choice from the list

	if answer['pawn'] == 'Top left':
		TTT[0,0] = 1
	elif answer['pawn'] == 'Top middle':
		TTT[0,1] = 1
	elif answer['pawn'] == 'Top right':
		TTT[0,2] = 1
	elif answer['pawn'] == 'Middle left':
		TTT[1,0] = 1
	elif answer['pawn'] == 'Middle':
		TTT[1,1] = 1
	elif answer['pawn'] == 'Middle right':
		TTT[1,2] = 1
	elif answer['pawn'] == 'Bottom left':
		TTT[2,0] = 1
	elif answer['pawn'] == 'Bottom middle':
		TTT[2,1] = 1
	elif answer['pawn'] == 'Bottom right':
		TTT[2,2] = 1

	print(TTT)

def TicTacToeCPU():
	print('Player is CPU, waiting for choice')
	time.sleep(3)
	global Player
	Player = 'CPU'
	CPU_choice = random.choice(position) 
	print('CPU choose : {}'.format(CPU_choice))
	position.remove(CPU_choice)#Remove the choice from the list

	if CPU_choice == 'Top left':
		TTT[0,0] = 2
	elif CPU_choice == 'Top middle':
		TTT[0,1] = 2
	elif CPU_choice == 'Top right':
		TTT[0,2] = 2
	elif CPU_choice == 'Middle left':
		TTT[1,0] = 2
	elif CPU_choice == 'Middle':
		TTT[1,1] = 2
	elif CPU_choice == 'Middle right':
		TTT[1,2] = 2
	elif CPU_choice == 'Bottom left':
		TTT[2,0] = 2
	elif CPU_choice == 'Bottom middle':
		TTT[2,1] = 2
	elif CPU_choice == 'Bottom right':
		TTT[2,2] = 2

	print(TTT)


while Player_score != 1:
#Set winning combinations
	if TTT[0,0] == 1 and TTT[0,1] == 1 and TTT[0,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[1,0] == 1 and TTT[1,1] == 1 and TTT[1,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[2,0] == 1 and TTT[2,1] == 1 and TTT[2,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,0] == 2 and TTT[0,1] == 2 and TTT[0,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[1,0] == 2 and TTT[1,1] == 2 and TTT[1,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[2,0] == 2 and TTT[2,1] == 2 and TTT[2,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,0] == 2 and TTT[1,0] == 2 and TTT[2,0] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,1] == 2 and TTT[1,1] == 2 and TTT[2,1] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,2] == 2 and TTT[1,2] == 2 and TTT[2,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,0] == 1 and TTT[1,0] == 1 and TTT[2,0] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,1] == 1 and TTT[1,1] == 1 and TTT[2,1] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,2] == 1 and TTT[1,2] == 1 and TTT[2,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,0] == 1 and TTT[1,1] == 1 and TTT[2,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,2] == 1 and TTT[1,1] == 1 and TTT[2,0] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,0] == 2 and TTT[1,1] == 2 and TTT[2,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,2] == 2 and TTT[1,1] == 2 and TTT[2,0] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	else:
		if Player == 'Player':
			TicTacToeCPU()
		else:
			TicTacToePlayer()




######################TWO PLAYERS########################

import numpy as np 
import inquirer 
import random 
import time

TTT = np.zeros((3,3)) #Create a matrix of 3 empty rows and columns --> for numbers

Players = ['Player1', 'Player2']
Player = random.choice(Players)

#Set possible places

position = ['Top left', 'Top middle', 'Top right', 'Middle left', 'Middle', 'Middle right', 'Bottom left', 'Bottom middle', 'Bottom right'] #Write all possible places

Player_score = 0

def TicTacToePlayer1():
	print('Player is 1, choose where to place your pawn')
	global Player
	Player = 'Player1'
	#Ask question
	questions = [ #open inquirer
  inquirer.List('pawn', #name of whats inquired
                message="Where do you want to place your pawn?", #ask your question
                choices=position, #choices are the positions
            ),
	]
	answer = inquirer.prompt(questions) #make the choice
	print(answer["pawn"]) #print the choice

	#Process the answer

	position.remove(answer['pawn'])#Remove the choice from the list

	if answer['pawn'] == 'Top left':
		TTT[0,0] = 1
	elif answer['pawn'] == 'Top middle':
		TTT[0,1] = 1
	elif answer['pawn'] == 'Top right':
		TTT[0,2] = 1
	elif answer['pawn'] == 'Middle left':
		TTT[1,0] = 1
	elif answer['pawn'] == 'Middle':
		TTT[1,1] = 1
	elif answer['pawn'] == 'Middle right':
		TTT[1,2] = 1
	elif answer['pawn'] == 'Bottom left':
		TTT[2,0] = 1
	elif answer['pawn'] == 'Bottom middle':
		TTT[2,1] = 1
	elif answer['pawn'] == 'Bottom right':
		TTT[2,2] = 1

	print(TTT)

def TicTacToePlayer2():
	print('Player is 2, choose where to place your pawn')
	global Player
	Player = 'Player2'
	#Ask question
	questions = [ #open inquirer
  inquirer.List('pawn', #name of whats inquired
                message="Where do you want to place your pawn?", #ask your question
                choices=position, #choices are the positions
            ),
	]
	answer = inquirer.prompt(questions) #make the choice
	print(answer["pawn"]) #print the choice

	#Process the answer

	position.remove(answer['pawn'])#Remove the choice from the list

	if answer['pawn'] == 'Top left':
		TTT[0,0] = 2
	elif answer['pawn'] == 'Top middle':
		TTT[0,1] = 2
	elif answer['pawn'] == 'Top right':
		TTT[0,2] = 2
	elif answer['pawn'] == 'Middle left':
		TTT[1,0] = 2
	elif answer['pawn'] == 'Middle':
		TTT[1,1] = 2
	elif answer['pawn'] == 'Middle right':
		TTT[1,2] = 2
	elif answer['pawn'] == 'Bottom left':
		TTT[2,0] = 2
	elif answer['pawn'] == 'Bottom middle':
		TTT[2,1] = 2
	elif answer['pawn'] == 'Bottom right':
		TTT[2,2] = 2

	print(TTT)


while Player_score != 1:
#Set winning combinations
	if TTT[0,0] == 1 and TTT[0,1] == 1 and TTT[0,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[1,0] == 1 and TTT[1,1] == 1 and TTT[1,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[2,0] == 1 and TTT[2,1] == 1 and TTT[2,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,0] == 2 and TTT[0,1] == 2 and TTT[0,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[1,0] == 2 and TTT[1,1] == 2 and TTT[1,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[2,0] == 2 and TTT[2,1] == 2 and TTT[2,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,0] == 2 and TTT[1,0] == 2 and TTT[2,0] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,1] == 2 and TTT[1,1] == 2 and TTT[2,1] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,2] == 2 and TTT[1,2] == 2 and TTT[2,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,0] == 1 and TTT[1,0] == 1 and TTT[2,0] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,1] == 1 and TTT[1,1] == 1 and TTT[2,1] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,2] == 1 and TTT[1,2] == 1 and TTT[2,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,0] == 1 and TTT[1,1] == 1 and TTT[2,2] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,2] == 1 and TTT[1,1] == 1 and TTT[2,0] == 1:
		Player_score = 1
		print("\033[92m You won\033[0m")
	elif TTT[0,0] == 2 and TTT[1,1] == 2 and TTT[2,2] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	elif TTT[0,2] == 2 and TTT[1,1] == 2 and TTT[2,0] == 2:
		Player_score = 1
		print("\033[91m You loose\033[0m")
	else:
		if Player == 'Player1':
			TicTacToePlayer2()
		else:
			TicTacToePlayer1()



#################### SECOND TRY ############################

import inquirer 
import random 
import time

Board = [' ' ,' ',' ',' ',' ',' ',' ',' ',' ']

def Board_setup(Board):
	print(' {} '.format(Board[0]),'|  {} '.format(Board[1]),'|  {} '.format(Board[2]))
	print('--------------')
	print(' {} '.format(Board[3]),'|  {} '.format(Board[4]),'|  {} '.format(Board[5]))
	print('--------------')
	print(' {} '.format(Board[6]),'|  {} '.format(Board[7]),'|  {} '.format(Board[8]))

position = {'Top left':0,'Top middle':1,'Top right':2,'Middle left':3,'Middle':4,'Middle right':5,'Bottom left':6,'Bottom middle':7,'Bottom right':8}

def Player_Win(Board):
	return (Board[0] == 'X' and Board[1] == 'X' and Board[2] == 'X') or (Board[3] == 'X' and Board[4] == 'X' and Board[5] == 'X')\
 	or (Board[6] == 'X' and Board[7] == 'X' and Board[8] == 'X') or (Board[3] == 'X' and Board[4] == 'X' and Board[5] == 'X')\
 	or (Board[0] == 'X' and Board[3] == 'X' and Board[6] == 'X') or (Board[1] == 'X' and Board[4] == 'X' and Board[7] == 'X')\
 	or (Board[2] == 'X' and Board[5] == 'X' and Board[8] == 'X') or (Board[0] == 'X' and Board[4] == 'X' and Board[8] == 'X')\
 	or (Board[2] == 'X' and Board[4] == 'X' and Board[6] == 'X')

def CPU_Win(Board):
	return (Board[0] == 'O' and Board[1] == 'O' and Board[2] == 'O') or (Board[3] == 'O' and Board[4] == 'O' and Board[5] == 'O')\
 	or (Board[6] == 'O' and Board[7] == 'O' and Board[8] == 'O') or (Board[3] == 'O' and Board[4] == 'O' and Board[5] == 'O')\
 	or (Board[0] == 'O' and Board[3] == 'O' and Board[6] == 'O') or (Board[1] == 'O' and Board[4] == 'O' and Board[7] == 'O')\
 	or (Board[2] == 'O' and Board[5] == 'O' and Board[8] == 'O') or (Board[0] == 'O' and Board[4] == 'O' and Board[8] == 'O')\
 	or (Board[2] == 'O' and Board[4] == 'O' and Board[6] == 'O')

def Tie(Board):
	return (Board[0] == 'X' or 'O') and (Board[1] == 'X' or 'O') and(Board[2] == 'X' or 'O') and(Board[3] == 'X' or 'O')\
 	and(Board[4] == 'X' or 'O') and(Board[5] == 'X' or 'O') and(Board[6] == 'X' or 'O') and(Board[7] == 'X' or 'O') and (Board[8] == 'X' or 'O')

Players = ['Human', 'CPU']
WhoPlays = random.choice(Players)

def TicTacToe(Board, WhoPlays):
	if WhoPlays == 'CPU':
		print('Player is CPU, waiting for choice')
		time.sleep(3)
		CPU_choice = random.choice(list(position)) 
		print('CPU choose : {}'.format(CPU_choice))
		Board[position[CPU_choice]] = 'O'
		del position[CPU_choice]
		time.sleep(1)
		Board_setup(Board)
		return 'Human'

	else:
		questions = [ #open inquirer
  	inquirer.List('pawn', #name of whats inquired
   	             message="Where do you want to place your pawn?", #ask your question
    	            choices=list(position), #choices are the positions
    	        ),
		]
		answer = inquirer.prompt(questions) #make the choice
		print('You chose')
		print(answer["pawn"])
		Board[position[answer["pawn"]]] = 'X'
		del position[answer["pawn"]]
		time.sleep(1)
		Board_setup(Board)
		return 'CPU'


while True:
	if Player_Win(Board) == True:
		print("\033[92m You won\033[0m")
		break
	elif CPU_Win(Board) == True:
		print("\033[91m You loose\033[0m")
		break
	elif Tie(Board) == True:
		print("No one wins")
		break
	else:
		WhoPlays = TicTacToe(Board, WhoPlays)









############### USING CLASS ##############

class board:
	def __init__(self):
		self.board = [' ' ,' ',' ',' ',' ',' ',' ',' ',' ']

	def Board_setup(board):
	print(' {} '.format(self.board[0]),'|  {} '.format(self.board[1]),'|  {} '.format(self.board[2]))
	print('--------------')
	print(' {} '.format(self.board[3]),'|  {} '.format(self.board[4]),'|  {} '.format(self.board[5]))
	print('--------------')
	print(' {} '.format(self.board[6]),'|  {} '.format(self.board[7]),'|  {} '.format(self.board[8]))