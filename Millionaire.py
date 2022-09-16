################## HEADER ################
#Code written by Anne-Lise Marais
#Contact at maraisannelise98 [at] gmail [dot] com

#Run the script to play Millionaire
#you can change questions and answers as wanted

##########################################

import time
def suspense():
	a = 3
	while a != 0:
			print(a)
			time.sleep(1)
			a=a-1
def Millionaire():
	player_life = 3
	Ans1 = "Earth"
	Ans2 = "One"
	Ans3 = "Yes"
	Ans4 = "Russia"
	Ans5 = "Paris"
	
	question = 1
	Question1 = "What's the name of our planet ?"
	Question2 = "How many moons does our planet have ?"
	Question3 = "Do you like Harry Potter ?"
	Question4 = "What's the biggest country ?"
	Question5 = "Capital city of France ?"

	while player_life != 0 and question < 6:
		
		if question == 1:
			print (Question1)
			player_choice = input("")
			if player_choice != Ans1:
				suspense()
				player_life -= 1
				print ("\033[91m You are slowly dying, remaining : {} \033[0m".format(player_life))
				print("\033[91m The end is near\033[0m")
			else:
				suspense()
				print("\033[92m Yes, next question\033[0m")
				question += 1
		elif question == 2:
			print(Question2)
			player_choice = input("")
			if player_choice != Ans2:
				suspense()
				player_life -= 1
				print ("\033[91m You are slowly dying, remaining : {}\033[0m".format(player_life))
				print("\033[91m The end is near\033[0m")
			else:
				suspense()
				print("\033[92m Yes, next question\033[0m")
				question += 1
		elif question == 3:
			print(Question3)
			player_choice = input("")
			if player_choice != Ans3:
				suspense()
				player_life -= 1
				print ("\033[91m You are slowly dying, remaining : {}\033[0m".format(player_life))
				print("\033[91m You muggle, try again\033[0m")
			else:
				suspense()
				print("\033[92m Welcome to Hogwarts ;) \033[0m")
				question += 1
		elif question == 4:
			print(Question4)
			player_choice = input("")
			if player_choice != Ans4:
				suspense()
				player_life -= 1
				print ("\033[91m You are slowly dying, remaining : {}\033[0m".format(player_life))
				print("\033[91m The end is near\033[0m")
			else:
				suspense()
				print("\033[92m Yes, next question\033[0m")
				question += 1
		else:
			print(Question5)
			player_choice = input("")
			if player_choice != Ans5:
				suspense()
				player_life -= 1
				print ("\033[91m You are slowly dying, remaining : {}\033[0m".format(player_life))
				print("\033[91m The end is near\033[0m")
			else:
				suspense()
				print("\033[92m Well done!\033[0m")
				question += 1
	if question == 6:
		print("\033[91m Winner !! \033[0m")
	else:
		print("\033[91m Looser\033[0m")