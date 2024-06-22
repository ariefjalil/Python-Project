# # ------------------------------------------------------
# # # #Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# # ------------------------------------------------------

# # # import random
# # # spam = 0
# # # num = random.randint(1,10)

# # # hello = 0
# # # howdy = 0
# # # greetings = 0

# # # while True:
# # # 	print('%s Hello, %s Howdy, %s Greetings' %(hello, howdy, greetings))

# # # 	for greetings in range (5): 
# # # 		if num == 1:
# # # 			spam = 1
# # # 			print('Hello')
# # # 			hello += 1

# # # 		elif num == 2:
# # # 			spam ==2
# # # 			print('Howdy')
# # # 			howdy += 1

# # # 		else:
# # # 			print('Greetings')
# # # 			greetings += 1

# # import random

# # spam = 0
# # num = random.randint(1, 10)

# # hello = 0
# # howdy = 0
# # greetings = 0

# # while hello < 10 and howdy < 10 and greetings < 10:  # Check all counters before loop
# #     print('%s Hello, %s Howdy, %s Greetings' % (hello, howdy, greetings))

# #     for _ in range(5):  # Use a throwaway variable for the loop
# #         if num == 1:
# #             spam = 1
# #             print('Hello')
# #             hello += 1
# #             if hello == 10:  # Check for hello reaching 10 and break
# #                 break

# #         elif num == 2:
# #             spam = 2
# #             print('Howdy')
# #             howdy += 1
# #             if howdy == 10:  # Check for howdy reaching 10 and break
# #                 break

# #         else:
# #             print('Greetings')
# #             greetings += 1
# #             if greetings == 10:  # Check for greetings reaching 10 and break
# #                 break

# # print("Program stopped!")




# # Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# # ------------------------------------------------------

# #for loop
# # ------------------------------------------------------


# # i = 0

# # for i in range(10):
# # 	i +=1
# # 	print(i)

# # ------------------------------------------------------
# # #while loop
# # ------------------------------------------------------


# # i = 0
# # while i < 10:
# # 	i+= 1

# # 	print(i)



# # ------------------------------------------------------
# #Introduction to def()
# # ------------------------------------------------------

# # def hello():
# # 	print('Howdy!')
# # 	print('Hello!')
# # 	print('Hello world!')


# # hello()
# # hello()
# # hello()

# # ------------------------------------------------------

# def hello(name):
# 	print ('Hello bitches '+name)


# hello('Cloud')
# hello('Squal')


# ------------------------------------------------------
# import random

# def getAnsw(ansNum):
# 	if ansNum == 1:
# 		return 'It is certain'
# 	elif ansNum == 2:
# 		return 'Gg my friend'

# 	else:
# 		return 'bye life'

# num = random.randint(1,3)
# print(getAnsw(num))

# ------------------------------------------------------
# CALL STACK
# ------------------------------------------------------

# a() starts
# b() starts
# c() starts
# c() returns
# b() returns
# d() starts
# d() returns
# a() returns



# def a():
# 	print('a() starts')
# 	b()
# 	d()
# 	print('a() returns')


# def b():
# 	print('b() starts')
# 	c()
# 	print('b() returns')

# def c():
# 	print('c() starts')
# 	print('c() returns')

# def d():
# 	print('d() starts')
# 	print('d() returns')

# b()

#------------------------------------------------------
#Local and Global Variables with the Same Name

#------------------------------------------------------



def spam():
	eggs = 'spam local'
	print(eggs)

def bacon():

	eggs = 'bacon local'
	print(eggs)
	spam()
	print(eggs)


eggs ='Global'

bacon()
print(eggs)



