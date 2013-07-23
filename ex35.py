# this is an adventure game, very similar to MUD/godwars back in the days.

from sys import exit
# we are using the sys module and importing the exit feature.
# exit from Python is implemented by raising the SystemExit exception, so cleanup actions specified by final clauses of try statements are honored,
# and it is possible to intercept the exit attempt.  In general, Exception is a bad idea.  You'll catch all kinds of stuff you don't want to catch -- like
# SystemExit -- and it can also mask your own programming errors.  

# This program starts from bottom to top (weird)

def gold_room():
	print "This room is full of gold.  How much do you take?"
	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.  You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()


# QUESTION: why does this program start from bottom to top? - BECAUSE you can't call a function until after you've defined it.
# the pattern of the defined function doesn't matter.  Only thing that matters is make sure the functions are defined before you can call it, which is why start() is at the bottom.

# Program layout in ENGLISH
# you start in a dark room and you're given 2 options to go (either left or right)
# left will bring you to the bear_room and right will bring you to the cthulhu_room.
# Let's start with the LEFT option first (bear_room)
# upon entering this room, you are given 3 messages.  1) There is a bear here.  2) bear has honey 3) fat bear is infront of another door. how are you going to proceed?  You ONLY have 2 options here (fleeing is not an option in this room but you will be able to later in the Cthulhul room)
# option 1 is "take honey" - and the result will be "bear looks at you then slaps your face off."
# option 2 is "taunt bear" - and the bear will move aside from the door.  You can then enter "open door" to proceed to the gold room (which will explain next)
# *****Note: if you try to "taunt bear" for a second time, the bear will "get pissed off and chews your lef off".

# assuming you taunt bear 1 time and opens the door to the "gold room" you will be told this room is full of gold.  How much do you take?
# *****Note: if you enter arbitrary characters like letters that are not recognized in this parameter range of (0-50), you will error out (exception, which is part of "import exit")
# if you enter 0-49, you will get back the message (Nice, you are not greedy, you win!)
# if you enter 50+, you will get back the message ("You greedy bastard!") and end up dying and lose.

# GOING BACK TO THE DARK ROOM, if you start at going right, you will end up at the cthulhu_room.
# there, you will get 3 messages.  1) Here you see the great evil Cthulhu 2) He, it, whatever stares at you and you go insane.  3) do you flee for your life or eat your head?
# option 1 is "flee" and you will be going back to the dark room where you started and have the options of going left or right again.
# option 2 is "eat your head" and you will get back the message "Well that was tasty" and you die and lose.

# NOTICE1: entering words/characters not recognized in each part of the program will return the "else" statement in each function.
# NOTICE2: proper exiting of the program will be reflected by exit(0). On many operating systems  a program can abord with exit(0), and the number passed in will indicate an error or not.
#			If you do exit(1) then it will be an error, but exit(0) will be a good exit.  The reason it's backward from normal boolean logic (with0==False is that you can use different numbers 
#			indicate error results.  Such as you can do exit(100) for a different error result than exit(2) or exit(1))
# NOTICE3: while True makes an infinite loop.




