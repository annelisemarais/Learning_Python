#Create a Tic Tac Toe



##Brainstorming
##Create a 3*3 matrix, no user interface, have a prompt asking where you put your X, randomized whos X and O (first player), create a rule "3 in line = victory", no space = par, 


import numpy as np #import numpy

	#First, create a matrix

M = np.arange(10) #It's a vector, need a 2D matrix

M2 =  np.random.randint(1, 10, size=(3, 3)) #creates a 2D matrix with size 3*3 and random numbers btw 1 and 10

	#Understand how indexing works in a matrix, 0 base indexing !!!!!

M2[0,2] #Returns first row, third column number

	#Create an empty array for STRINGS

TTT = np.zeros((3,3)) #Create a matrix of 3 empty rows and columns --> for numbers

#TTT = np.chararray((3, 3))
#TTT[:] = '.'

#TTT = [['.','.','.'],['.','.','.'],['.','.','.']]


	
pip install inquirer #add an inquirer
import inquirer #import inquirer

#Set possible places

position = ['Top left', 'Top middle', 'Top right', 'Middle left', 'Middle', 'Middle right', 'Bottom left', 'Bottom middle', 'Bottom right'] #Write all possible places

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



