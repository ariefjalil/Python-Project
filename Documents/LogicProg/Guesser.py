import random

Rand = random.randint(1,100)

while True:
    print "Guess a number between 1 and 100."
    guess = int(raw_input ("Your guess:"))
    if guess == Rand:
        print "You got it!"
        break
    elif guess > Rand:
        print "Choose lower."
    elif guess < Rand:
        print "Choose higher."
        
