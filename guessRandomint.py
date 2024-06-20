import random
print('I am thinking of a number between 1 and 20')
number = random.randint(1,20)

#Ask player to guess 6 times

for guessTaken in range(1,7):
	print('Take a guess')
	user_guess = int(input('>'))

	if user_guess < number:
		print('Your number is too low')
		continue #This is not necessary as the input is under for loop
	elif user_guess > number:
		print('Your number is too high')
	
	else:
		break #This condition is the correct guess. Break the loop


	# elif user_guess == number:
	# 	print('Good job!')
	# break

if user_guess == number:
	print('Good job! You guess my number in ' +str(guessTaken)+     ' guesses!')

else:
	print('Nope the number I was thinking of was ' +str(number))