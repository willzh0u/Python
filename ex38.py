# Exercise 38

# variable ten_things = the string of "Apples Oranges Crows Telephone Light Sugar"
ten_things = "Apples Oranges Crows Telephone Light Sugar"
# this is just printing a string.
print "Wait there's not 10 things in that list, let's fix that."
# before we get started, we're setting the variable "stuff" = to what ten_things split by quotes would be.
stuff = ten_things.split(' ')
# more stuff is a new variable and it's defined by the already seperated elements from the list.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# here, while the lenghth of items in "stuff" (which is ten_things all split up) is not equal to 10:
# Note: this function will run until "while len(stuff) != 10" is no longer true meaning it will stop at 10. 
while len(stuff) != 10:
	# remember .pop() removes the last element from a list.
	# set new variable next_one = more_stuff.pop() so we'll be taking the last element from this list of items each time.
	next_one = more_stuff.pop()
	# just printing a string here and adding the "next_one" element that we take out of more_stuff and adding to the ten_things() list.
	print "Adding: ", next_one
	# we are actually appending the stuff variable with the element taken out with .pop() from more stuff.
	stuff.append(next_one)
	# each time we add a new item, we will get a new count of total items in the list with %d, which is sort of defined by the new length of "stuff"
	print "There's %d items now." % len(stuff)

# Once function hits 10, it will stop and print the new list of "stuff" with all new items added to list.
print "There we go: ", stuff
# just a string
print "Let's do some things with stuff."
# printing the "stuff" item at the 1 position.  remember. there's also 0 so the item at 1 will be oranges
print stuff[1]
# similar to above, we are going backwards with -1 so it's Corn.  Remember, there's still 0!
print stuff[-1] # whoa!  fancy!
# remember, .pop() just takes the last element out.  Since we're not adding it anywhere else, we're just shortening "stuff".  So "Corn" get's "pop'ed"
print stuff.pop()
# We are joining "stuff" with ' ' between them.  Now we are joining all the items minus corn that was taken out last back into a string.  
print ' '.join(stuff) # what?  cool!
# Note: this is just a 'slice' from the "stuff" list that is from element 3 to element 4, meaning it does not include element 5.  it's similar to how range (3,5) would work where only 3 and 4 are referenced and not 5.
print '#'.join(stuff[3:5]) # super stellar!


# WHAT IS DIR
# In python, dir is a built-in function.  It gives a directory of all attributes of an object.  
# for example: 
# 		import odbchelper
#		dir(odbhelper)
#		['_builtins_', '_doc_', '_file_', '_name_', 'buildConnectionString']

# difference between class and dir() = dir() gives more information than the old one.  dir() on a class shows the contents of the _dict_ of the class and all its base classes.  
# It does not show class attributes that are defined by a metaclass.

# Python 2.2 has 2 type of classes: classic of old-style classes and new classes.  Old class model is exactly the same as older versions and dropped in Python 3.0.
# Most of python's built-in tpyes, such as integers, lists, dictionaries, and even files, are new stlyes now.
# A new-style class named object, the base class for all built-in types, has also been added so if no built-in type is suitable, you can just subclss object:

# class C(object):
	# def _init_ (self):

# type objects for the built-in types are avaialble as built-ins named using a clever trick.  Python has always had built-in functions int(), float(), and str().  
# >>> int
# <type 'int'>
# >>> int('123')
# 123

# In Python, enter dir() or int ().
# for dir(), you will see ['_builtins_', '_doc_', '_file_', '_name_', 'buildConnectionString']
# If you enter dir(__name__) for example, you will see the directories inside the __name__ directory.

