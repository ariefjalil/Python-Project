import random
print('i am thinking of a number between 1 and 20')
number = random.randint(1,20)

for guessNum in range(1,7):
	print('Take a guess')
	user_guess = int(input('>'))

	if user_guess < number:
		print('Your guess is too low.')

	elif user_guess > number:
		print('Your guess is too high.')

	else:
		break

if user_guess == number:
	print('Good job! You guessed my number in ' +str(guessNum)+ ' guesses!')

else:
	print('Too bad! The number I was thinking of was ' +str(number))