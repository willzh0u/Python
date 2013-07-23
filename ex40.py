# ex40, Modules, Classes, And Objects (Object Oriented Programming).
# What does Object Oriented Programming mean?
#	There's a construct in Python called a class that lets you structure your software in a particular way.
#	Using classes you an add consistency to your programs so that they can be used in a cleaner way/

# Modules are like Dictionaries

# # example 1 (mute other examples if you want to use this one)
# mystuff = {'apple': "I am apples!"}
# print mystuff['apple']

# Modules have these 3 characteristics
#	1) A PYthon file with some functions or variables in it
#	2) You then import that file.
#	3) And then you access the functions or variables in that module with the '.'(dot) operator.

# example 2

# this goes in mystuff.py (import mystuff.py because it's an actual file that I created earlier!)

# referring back to dicationary, and I should start to see how this is similar to using a dicationary, but the syntax is different.

#	mystuff['apple'] # is to get apple from dict
#	mystuff.apple() # get apple from the module
#	mystuff.tangerine # same thing, it's just a variable

# This means we have a very common pattern in Python of this:
#	1. Take a key=value style container.
#	2. Get something out of it by the key's name.

# In the case of the dictionary, the key is a string and the syntax is a [key].  
# In the case of the module, the keys is an identifier, and the syntax is .key.  Other than that they are nearly the same thing.

# Classes are like modules.
#	A way to think about modules is they are a specialized dictionary that can store Python code so you can get to it with the '.' (dot) operator
#	Python also has another construct that serves a purpose called a class.  A class is a way to take a grouping of functions and dicationary
#	and place them inside a container so you can access them with the '.' opreator.

# example: (mute other examples if you want to use this one) If I were to create a class just like the myself module, I'd do something like this:

# class MyStuff(object):
#	def _init_(self):
		# self.tangerine = "And now a thousand years between"
	# def apple(self):
		# print "I AM CLASSY APPLES!"

# Objects are like mini imports.
#	there has to be a similar concept to import but for classes.  The concept is called "instantiate" which means create.  
# 	when you instantiate a class, you get an object.

# example (mute other examples if you want to use this one)

# thing = mystuff note: don't include the () like example shown in tutorial
# thing.apple()
# print thing.tangerine

# A first class example (mute other examples if you want to use this one)

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
happy_bday = Song(["Happy Birthday to you",
					"I don't want to get sued",
					"So I 'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# why do I need self when I make __init__ or other functions for classes?
#	If you don't have self, then code like cheese = 'Frank' is ambiguous.  That code isn't clear about whether you mean the instance's cheese attribute, or a local variable named cheese.  
#	With self.cheese = 'Frank' it's very clear you mean the instance attribute self.cheese