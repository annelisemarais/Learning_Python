#Create a Tic Tac Toe



####################Brainstorming######################
##Create a 3*3 matrix, no user interface, have a prompt asking where you put your X, randomized whos X and O (first player), create a rule "3 in line = victory", no space = par, 


	#First, create a matrix

M = np.arange(10) #It's a vector, need a 2D matrix

M2 =  np.random.randint(1, 10, size=(3, 3)) #creates a 2D matrix with size 3*3 and random numbers btw 1 and 10

	#Understand how indexing works in a matrix, 0 base indexing !!!!!

M2[0,2] #Returns first row, third column number

	#Create an empty array for STRINGS


#TTT = np.chararray((3, 3))
#TTT[:] = '.'

#TTT = [['.','.','.'],['.','.','.'],['.','.','.']]




###################TIC TAC TOE###########################
####################FIRST TRY############################
	
pip install inquirer #add an inquirer


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