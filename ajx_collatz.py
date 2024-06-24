

def collatz():

	print('Enter number:')
	user_input = int(input('> '))

	while user_input != 1:
		if user_input %2 == 0:
			user_input //=2


		else:
			user_input = 3 * user_input + 1
		print(user_input)


collatz()