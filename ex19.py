
# defining the variable cheese_and_crackers with cheese_count and boxes_of_crackers variables/arguments.
# this is sort of like the set foundation of the script.  The rest of the print commands below are different ways to run this script.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# %d is used for decimal or number is an integer.
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	# /n will break a line between the code.
	print "Get a blanket. \n"


# this is just plugging numbers into cheese_count and boxes_of_crackers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# here, we are actually defining cheese_and_crackers with 2 new variables. 
# and both of these arguments are defined (=) by values (of 10 & 50)

# these variables live INSIDE the function.  (cheese_count & boxes_of_crackers live outside)

#When the function exits these temporary variables go away and everything keeps working. 
#Keep going in the book and this should become clearer.

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50


cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# using the defined variable "cheese_and_crackers" and the original variables/arguments,
# we are just doing math within paranthesis
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# combining variables with math inside the script.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


#*************MY FUNCTION**********************

def chips_and_salsa(chips_count, jars_of_salsa):
	print "You have %d bags of chips!" % chips_count
	print "You have %d jars of salsa as well!" % jars_of_salsa
	print "That's enough for a party!"
	print "Get the table ready! \n"


print "We can just apply function numbers directly:"
chips_and_salsa(10, 20)


print "OR, we can use variable from our script!"
amount_of_chips = 5
amount_of_salsa = 10

chips_and_salsa(amount_of_chips, amount_of_salsa)


print "OR, we can do some math here!"
chips_and_salsa(5 + 10, 20 + 50)

print "OR, even combine variables and math together!"
chips_and_salsa(amount_of_chips + 5000000, amount_of_salsa + 100000000)


print "OR even use variables of variables!"
amount_of_chips = amountchips = 9999
# amountchips = 9999

amount_of_salsa = amountsalsa = 7777
# amountsalsa = 7777

chips_and_salsa(amountchips, amountsalsa)


#*******THIS IS COMPLETELY PRO FROM MY END!*******
# prompt is used below as an indicator for answer in terminal.
prompt = '>'

print "OR, how about you tell me how many bags of chips do you have?"
chips = raw_input(prompt)


print "Now, tell me about how many jars of salsa do you have?"
salsa = raw_input(prompt)

# I don't understand how come I can use %s and %r below, but not %d, while %d works in the first function.
# ****NOTE/UPDATE: adding int(chips), int(salsa) converts the raw input into integers that will allow us to use %d !!!!!
print "Ok so it looks like you have %d bags of chips and %d jars of salsa!" % (int(chips), int(salsa))






