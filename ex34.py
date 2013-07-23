# Accessing Elements of Lists

# REMEMBER: Python start its lists at 0 rather than 1.
# ordinal numbers, because they indicate an ordering of things.  Ordial numbers tell the order of things in a set, first, second, third.
# cardinal numbre means you can pick at random, so there needs to be a 0 element. Cardial numbers tells how many.  

# everytime you want the 3rd animal, you translate this "ordinal" number to a "cardinal" number by subtracting 1.
# the 3rd animal is at idnex 2 and is the penguin.
# you have to do this because you have spent your whole life using ordinal numbers, and you have to think in cardinal.  
# Just subtract 1 and you will be good.

# REMEMBER: ordinal == ordered, 1st; cardinal == cards at random, 0.


animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
# bear = animals[0]
# python = animals[1]
# peacock = animals[2]
# kangaroo = animals[3]
# whale = animals[4]
# platypus = animals[5]

print 'There are 6 animals in the race, enter a number to find our which animal finished in that place:'

while True:
	rank = int(raw_input())
	print "Number %d animal is: %s" % (rank, animals[rank - 1]) 



# 1. The animal at 1.
# # The 2nd animal is at 1 and is a Python.  The animal at 1 is the 2nd animal and is a Python.
# 2. The 3rd animal.
# # the 3rd animal is at 2 and is a Peacock.  The animal at 2 is the 3rd animal and is a Peacock.
# 3. The 1st animal.
# # the 1st animal is at 0 and is a bear.  The animal at 0 is the 1st animal and is a bear.
# 4. The animal at 3.
# # the animal at 3 is the 4th animal and is a kangaroo.  The 4th animal is at 3 and is a kangaroo.
# 5. The 5th animal.
# # the animal at 4 is the 5th animal and is a whale.  The 5th animal is at 4 and is a whale.
# 6. The animal at 2.
# # the animal at 2 is the 3rd animal and is peacock.  The 3rd animal is at 2 and is a peacock.
# 7. The 6th animal.
# # the 6th animal is at 5 and is a platypus.  The 6th animal is at 5 and is a platypus.
# 8. The animal at 4.
# # the animal at 4 is the 5th animal and is a whale.  The 5th animal is at 4 and is a whale.
