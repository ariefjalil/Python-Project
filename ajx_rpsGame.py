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

while True: #main game loop
	print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))

	while True:
		print('Enter your your move: (r)ock (p)aper (s)cissors (q)uit')
		user_input = input('>')
		if user_input == 'q':
			sys.exit()
		if user_input == 'r' or user_input=='p' or user_input=='s':
			break
		print('Type one of r, p, s, or q.')
		

	if user_input == 'r':
		print('Rock versus ...')
	elif user_input == 'p':
		print('Paper versus ...')
	elif user_input == 's':
		print('Scissors versus...')


	#computer move
	computer = random.randint(1,3)

	if computer == 1:
		comGuess = 'r'
		print('ROCK!')

	elif computer == 2:
		comGuess = 'p'
		print('PAPER!')

	elif computer == 3:
		comGuess = 's'
		print('Scissors!')


	if user_input == comGuess:
		print(f'It\'s a TIE. You both chose {user_input}')
		ties += 1


		#simpliy the code

	elif (user_input == 'r' and comGuess =='s') or (user_input == 'p' and comGuess == 'r') or \
		(user_input == 's' and comGuess == 'p') :
		print('YOU WIN!🥇')
		wins += 1

	else:

		print('YOU LOSE!😭')
		losses += 1


	# elif user_input == 'r' and comGuess =='s':
	# 	print('YOU WIN!🥇')
	# 	wins += 1

	# elif user_input == 'p' and comGuess =='r':
	# 	print('YOU WIN!🥇')
	# 	wins += 1

	# elif user_input == 's' and comGuess =='p':
	# 	print('YOU WIN!🥇')
	# # 	wins += 1
	# elif user_input == 'r' and comGuess =='p':
	# 	print('YOU LOSE!😭')
	# 	losses += 1

	# elif user_input == 'p' and comGuess =='s':
	# 	print('YOU LOSE!😭')
	# 	losses += 1

	# elif user_input == 's' and comGuess =='r':
	# 	print('YOU LOSE!😭')
	# 	losses += 1

