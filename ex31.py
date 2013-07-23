# this is an adventure game.  This is interesting because it can potentially be how our helpcenter is written in Python.  
# 1.  pop a question ""You enter a dark room with two doors.  Do you go through door #1 or door #2?""
# 2.  the player will choose either 1, 2, or a random answer.  
# 3.  entering 1, will print the next question for option 1: "There's a giant bear here eating a cheese cake.  What do you do?" and will present you with 2 more options.
# 4.  entering 2, will print the next question for option 2: "You stare into the endless abyss at Cthulhu's retina." and will present you with 3 more options.
# 5.  If you entered neither a 1 or 2, you will get response 3: "You stumble around and fall on a knife and die.  Good job!"
# 6.  remember, each elif is an option!

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake.  What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off.  Good job!"
	elif bear == "2":
		print "The bear eats your legs off.  Good job!"
	else:
		print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives by a mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "3":
	print "There's a golden chest waiting for you to open. .. ... ....what do you do?"
	print "1. Open it"
	print "2. Leave it"

	hungry = raw_input("> ")

	if hungry == "1":
		print "You are are rewarded with a bite from a snake! Ouch!"
	elif hungry == "2":
		print "Good job for not opening, you found some food 10 ft away"
	else:
		print "Wish you were more decisive here..."


else:
	print "You stumble around and fall on a knife and die.  Good job!"




# Can you replace elif with a sequence of if/else combinations?
#		You can in some situations, but it depends on how each if/else is written.  It also means that Python will check every if/else
#		combination, rather than just the first false ones like it would with if/elif/else.  

# How do I tell if a number is between a range of numbers?
#		You have 2 options: Use 0 < x < 10 or 1 <= x < 10 which is classic notation, or use x in range(1, 10).

# What if I wanted more options in the if/elif/else blocks?
#		Easy, just add more elif blocks for each possible choice.
