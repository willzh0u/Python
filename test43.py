from random import randint
import pdb

guess = raw_input("[keypad]> ")

lottonumbers = randint(1,9)
# print lottonumbers

if guess == lottonumbers:
	print("you win!")
else:
	print ("Sorry the correct number is actually '%d'") % lottonumbers

# references:
# http://stackoverflow.com/questions/3996904/python-generate-random-integers-between-0-and-9
# http://stackoverflow.com/questions/5990928/learning-python-couldnt-figure-out-random-randint
# http://stackoverflow.com/questions/5075430/python-classes-in-2-files-learn-python-the-hard-way



# def lotto(numbers):
# 	# numbers = raw_input("[keypad]> ")
# 	lottonumbers = randint(1,9)

# 	print lottonumbers
	


	# if numbers == lottonumbers:
	# 	print("you're a winner!")
	# else:
	# 	print lottonumbers













# from random import randint
# import pdb

# def lottery():
# 	win = True
# 	for i in range(3):
# 		guess = random.randint(1,100)
# 		if int(raw_input("Please enter a number...")) != guess:
# 			win = False
# 			break
# 	return win







# from random import randint

# def lotto(numbers):
# 	# make a lotto list
# 	lottonumbers = "%d" % randint(1,9)
# 	# numbers = raw_input("[keypad> ")

# 	# if numbers == lottonumbers:
# 	# 	print("you're a winner!")
# 	# else:
# 	# 	print("better luck next time!")

# print lottonumbers






	# if numbers != lottonumbers:
	# 	print ("Sorry, better luck next time!")
	# 	numbers = raw_input("[keypad]> ")

	# # check to see if the numbers were equal to the lotto numbers
	# elif numbers == lottonumbers:
	# 	print ("you're a winner!") 

	# else:
	# 	print lottonumbers


# example 2:


