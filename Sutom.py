################## HEADER ################
#Code written by Anne-Lise Marais
#Contact at maraisannelise98 [at] gmail [dot] com

#Run the script to play SUTOM with CPU

#requires !pip install english-words

##################### SUTOM ####################

import random
from english_words import english_words_lower_alpha_set as allwords
from colorama import Fore, Back, Style

rules = 'You will have to find a word randomly chose. Only write lower-case words.\n \
Plural and conjugated words are not valid\n \
If the letter is not in the word, it will be displayed in red\n \
If the letter is in the word but not in the right place, it will be displayed in yellow\n \
If the letter is in the word, in the right place, is will be displayed in green'

word = random.choice(list(allwords))

length = len(word)

dispword = '_ ' * length
dispwordlist = list('_'*length)


print(rules+ '\n')
print("The word you are looking for has {} letters, best of luck !".format(length))
print(dispword)


def wordcheck(playerchoice):
	if len(playerchoice) != length:
		print('Enter a {} letters word'.format(length))
		playerchoice = input("")
	elif playerchoice not in allwords:
		print('Enter a valid word')
		playerchoice = input("")

def wordcomparison(playerchoice, word):
	index = 0
	print('You chose:')
	for letter in playerchoice:
		if letter not in word:
			print(Fore.RED + letter, end =" ")
			print(Style.RESET_ALL, end =" ")
		else:
			if playerchoice[index] == word[index]:
				dispwordlist[index] = letter
				print(Fore.GREEN + letter, end =" ")
				print(Style.RESET_ALL, end =" ")
			else:
				print(Fore.YELLOW + letter, end =" ")
				print(Style.RESET_ALL, end =" ")
		index = index+1
	word2find = ''.join(dispwordlist)
	print('\n')
	print('Word to find:\n')
	for letter in word2find:
		print(letter, end =" ")

playerchoice = ''

while True:
	if playerchoice != word:
		playerchoice = input("")
		wordcheck(playerchoice)
		wordcomparison(playerchoice,word)
	else:
		print('Bravo')
