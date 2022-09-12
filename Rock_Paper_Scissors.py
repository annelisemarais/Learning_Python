import random
import time
def RPC():
	player_score = 0
	cpu_score = 0

	while player_score != 3 and player_score != 3:
		player_choice = int(input("Rock (1), Paper (2), Scissors (3) ?"))
		cpu_choice = random.choice([1, 2, 3])
		if player_choice == 1:
			player_choice_name = 'Rock'
		elif player_choice == 2:
			player_choice_name = 'Paper'
		else:
			player_choice_name = 'Scissors'
		if cpu_choice == 1:
			cpu_choice_name = 'Rock'
		elif cpu_choice == 2:
			cpu_choice_name = 'Paper'
		else:
			cpu_choice_name = 'Scissors'
		print("Your choice : {}, CPU choice: {}".format(player_choice_name, cpu_choice_name))
		time.sleep(2)
		if player_choice == cpu_choice:
			print("Tie")
		elif player_choice == 1 and cpu_choice == 2:
			print("You loser")
			cpu_score += 1
		elif player_choice == 1 and cpu_choice == 3:
			print ("You win !")
			player_score += 1
		elif player_choice == 2 and cpu_choice == 1:
			print ("You win !")
			player_score += 1
		elif player_choice == 2 and cpu_choice == 3:
			print ("You loser")
			cpu_score += 1
		elif player_choice == 3 and cpu_choice == 1:
			print ("You loser")
			cpu_score += 1
		elif player_choice == 3 and cpu_choice == 2:
			print ("You win !")
			player_score += 1
		print ("Your score : {}, cpu score : {}".format(player_score,cpu_score))
	if player_score == 3:
		print("Bravo")
	else: 
		print("Try again")


######MODIFIED VERSION - CPU ALWAYS WIN##########

import time
def RPC():
		player_choice = int(input("Rock (1), Paper (2), Scissors (3) ?"))
		cpu_choice = (1, 2, 3)
		if player_choice == 1:
			player_choice_name = 'Rock'
			cpu_choice=2
		elif player_choice == 2:
			player_choice_name = 'Paper'
			cpu_choice=3
		else:
			player_choice_name = 'Scissors'
			cpu_choice=1
		if cpu_choice == 1:
			cpu_choice_name = 'Rock'
		elif cpu_choice == 2:
			cpu_choice_name = 'Paper'
		else:
			cpu_choice_name = 'Scissors'
		print("Your choice : {}, CPU choice: {}".format(player_choice_name, cpu_choice_name))
		time.sleep(2)
		if player_choice == 1:
			print("You owe me a drink")
		elif player_choice == 2:
			print("Take me to dinner")
		elif player_choice == 3:
			print("Nice try, but I win again")