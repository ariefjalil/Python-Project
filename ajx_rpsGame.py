# My take:

# import random

# myList = ["ROCK","PAPER","SCISSORS"]
# print('ROCK, PAPER, SCISSORS')

# cpuGuess=random.choice(myList)
# #user_input = myList

# while True:
# 	print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
# 	user_input= input('>')

# 	while user_input != "q":
# 		if user_input == "p":
# 			print('Paper versus.....')
# 			print(cpuGuess)
# 			break

# 		if user_input == 'r':
# 			print('Rock versus....')
# 			print(cpuGuess)
# 			break

# 		if user_input == 's':
# 			print('Scissors versus....')
# 			print(cpuGuess)


#actual answer

import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0




while True: # The main game loop.
	print('%s Wins, %s Losses, %s Ties' %(wins,losses, ties))


	while True: #player input loop
		print('Enter your move: (r)ock (p)aper (s)cissors (q)uit')
		user_input = input('>')
		if user_input == 'q':
			sys.exit() # Quit the program.

		if user_input == 'r' or user_input =='p' or user_input =='s':
			break # Break out of the player input loop if r p or s selected, else print below
		print('Please type r, p, s OR q')


	if user_input =='r':
		print('ROCK versus ...')
	elif user_input =='p':
		print('PAPER versus ...')
	elif user_input == 's':
		print('SCISSORS versus ...')

	#CPU selection
	randomNum = random.randint(1,3)
	if randomNum == 1:
		cpuGuess = 'r'
		print('ROCK!')
	elif randomNum == 2:
		cpuGuess ='p'
		print('PAPER!')
	elif randomNum == 3:
		cpuGuess = 's'
		print('SCISSORS!')


	if user_input == cpuGuess:
		print('It is a tie!')
		ties = ties + 1

	elif user_input == 'r' and cpuGuess =='s':
		print('You win!')
		wins = wins + 1

	elif user_input == 'p' and cpuGuess =='r':
		print('You win!')
		wins = wins + 1

	elif user_input == 's' and cpuGuess =='p':
		print('You win!')
		wins = wins + 1

	elif user_input == 'r' and cpuGuess =='p':
		print('You LOSE!')
		losses = losses + 1
	elif user_input == 'p' and cpuGuess =='s':
		print('You LOSE!')
		losses = losses + 1
	elif user_input == 's' and cpuGuess =='r':
		print('You LOSE!')
		losses = losses + 1






