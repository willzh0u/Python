# ex36.py
from sys import exit

def red_room_bonus():
	print "This room is full of treasure!  How much do you take?"
	next = raw_input(">>> ")

	how_much = int(next)

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		print "You greedy bastard!"
		exit(1)

def red_room():
	print "Here you just entered the red room and you see red leprechauns everywhere."
	print "These leprechauns are sneaky and will rob you before you know it, but they're weak."
	print "Do you \'run back\' or \'fight\'?"
	leprechaun_moved = False

	while True:
		next = raw_input(">>> ")

		if "run back" in next:
			start()
		elif "fight" in next:
			print "Congratulations, you just defeated all the leprechauns!  You can now \'open\' the secret red door!"
			leprechaun_moved = True
		elif "open" == next and leprechaun_moved:
			red_room_bonus()
		else:
			print "You're speaking nonsense!"

def blue_room_bonus():
		# print "Here is an animal race!  Enter a number to find out which animal finished in that place"
		print "You just entered a secret path from the blue room and there's a light at the end of the tunnel!"
		print "You can finally \'go home\' or \'go back\' to explore some more!"

		# animals = ['bear', 'python' 'peacock', 'kangaroo', 'whale', 'platypus']

		next = raw_input(">>> ")

		if "go home" in next:
			print "Well done, it's been a long game!"
			exit(0)
		elif "go back" in next:
			blue_room()
		else:
			print "So...what do you want to do?"

		


		while True:
			rank = int(raw_input(">>> "))
			print "Number %d animal is: %s" % (rank, animals[rank -1])




def blue_room():
	print "Here you just entered the blue room and you see blue monsters staring at you."
	print "These monsters have psychic powers that can paralyze you."
	print "Do you \'run back\' or \'fight\'?"
	blue_monsters_moved = False

	while True:
		next = raw_input(">>> ")

		if "run back" in next:
			start()
		elif "fight" in next:
			# dead("Now, why did you just try to do that?")
			print "Congratulations, you just defeated all of these monsters!  You can now \'open\' the secret blue door!"
			blue_monsters_moved = True
		elif "open" == next and blue_monsters_moved:
			blue_room_bonus()
		else:
			blue_room()

def green_room():
	print "Here you just entered the green room and you see green monsters staring at you."
	print "These monsters run real fast and will attack you quickly."
	print "Do you \'run back\' or \'fight\'?"

	next = raw_input(">>> ")

	if "run back" in next:
		start()
	elif "fight" in next:
		dead("Well, that was stupid.")
	else:
		green_room()



def dead(why):
	print why, "Good job!"
	exit(0)


def start():
	print "You are now in a dark room"
	print "There's a door in front of you, left, and right"
	print "Which one do you take?"

	next = raw_input(">>> ")

	if next == "front":
		red_room()
	elif next == "left":
		blue_room()
	elif next == "right":
		green_room()
	else:
		dead("You're walking around in circles and not going anywhere.  Hurry up.")



start()


























# ***NOTES****






# how can we use all of the above swiftly?

# from sys import argv
# from sys import exit
# from sys import os.path


# while loops
# from - loops

# - look at ex18
# use lists
# use functions
# use formatters

# raw_input

# 1) write up your idea for the game first.
# 1a create rooms
# 1b create monsters
# 1c create traps


# *** EXIT(0) = the optional argument arg can be an integer giving the exit status (defaulting to zero), or another type of object.  If it is an integer, zero is considfered "successful termination" 
# and any nonzero value is considered abnormal termination
