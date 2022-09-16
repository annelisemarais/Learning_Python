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

print(rules)
print('')
print("The word you are looking for has {} letters, best of luck !".format(length))
print(dispword)

dispplayerchoice = '_ ' * length

playerchoice = input("")

def wordcheck(playerchoice):
	if len(playerchoice) != length:
		print('Enter a {} letters word'.format(length))
		playerchoice = input("")
	elif playerchoice not in allwords:
		print('Enter a valid word')
		playerchoice = input("")

def wordcomparison(playerchoice, word):
	index = 0
	for letter in playerchoice:
		if letter not in word:
			print( 'Wrong letter: 'Fore.RED + letter)
			print(Style.RESET_ALL)
		else:
			if playerchoice[index] == word[index]:
				print(Fore.GREEN + letter)
				print(Style.RESET_ALL)
			else:
				print(Fore.YELLOW + letter)
				print(Style.RESET_ALL)
		index = +1




index = 0
for letter in playerchoice:
	if letter not in word:
		dispplayerchoice[index] = letter
	else:
		if playerchoice[index] == word[index]:
			dispplayerchoice[index] = letter
			dispword[index] = letter
		else:
			dispplayerchoice[index] = letter
			dispword[index] = letter
	index = +1

	dispplayerchoice[index].replace("_ ", letter)