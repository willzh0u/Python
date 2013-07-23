

# Implicit Inheritance
# class Parent(object): # this is a base class.  All subclasses beneath it will inherit all of its behavior from Parent.

# 	def implicit(self):
# 		print "PARENT implicit()"

# class Child(Parent):
# 	pass

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# The use of pass under the class Child: is how you tell Python that you want an empty block.  This creates a class named Child but says that there's nothing new to define in it.
# Instead it will inherit all of its behavior from Parent.  

# Notifce how even though I'm calling son.implicit() on line 16, and even though Child does not have a implicit function defined,
# it still works and it calls the one defined in Parent.  This shows you that, if you put functions in a base class (ie. Parent) then all subclasses (ie Child) will automatically get those features.  
# Very handy for repetitive code you need in many classes.



# Override Explicitly
# class Parent(object): # use override explicityly whenever you want the child to behave differently.  Remember, implicitly inheriting is continious repetition.  To do this, all you need to do is define Parent and Child class

# 	def override(self):
# 		print "PARENT override()"

# class Child(Parent):

# 	def override(self):
# 		print "CHILD override()"

# dad = Parent()
# son = Child()

# dad.override()
# son.override()

# The problem with implicitly having functions called is sometimes you want the child to behave differently.  In this case, you want to overrride the function in the child,
# effectively replacing the functionality.  To do this just define a function with the same name in Child.  

# In this example, I have a function named override in both classes.

# As you can see, when line 14 runs, it runs the Parent.override function because that variable (dad) is a Parent.
# But, when line 15 runs it prints out the Child.override messages because son is an instance of Child and child overrides that
# function by defining it's own version.


# Alter Before Or After
# class Parent(object):

# 	def altered(self):
# 		print "PARENT altered()"
# class Child(Parent):

# 	def altered(self):
# 		print "CHILD, BEFORE PARENT altered()"
# 		super(Child, self).altered()
# 		# notice super() is here for multi Inheritance
# 		print "CHILD, AFTER PARENT altered()"

# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()


# All three combined

# class Parent(object):

# 	def override(self):
# 		print "PARENT override()"

# 	def implicit(self):
# 		print "PARENT implicit()"

# 	def altered(self):
# 		print "PARENT altered()"

# class Child(Parent):

# 	def override(self):
# 		print "CHILD override()"

# 	def altered(self):
# 		print "CHILD, BEFORE PARENT altered()"
# 		super(Child, self).altered()
# 		print "CHILD, AFTER PARENT altered()"

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# dad.override()
# son.override()

# dad.altered()
# son.altered()

# The reason for super() = handles all of the complex MRO stuff where you need the altering type of actions as I did in Child.altered above.  With super() you don't have to worry about getting this right,
# and Python will find the right function for you.  

# Using super() With __init__
# The most common use of super() is actually in __init__ functions in base classes.  This is usually the only place where you need to do some things in a child,
# then complete the initialization in the parent.  

# class Child(Parent):

# 	def __init__(self, stuff):
# 		self.stuff = stuff
# 		super(Child, self).__init__

# this is pretty much the same as the Child.altered example above, except I'm setting some variables in the __init__ before having the Parent initialize with its Parent.__init__


# Composition; sorta like replicating interitance by just calling functions in a module.

class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()

# in this code, we're not using the name Parent, since there is not a parent-child is-a relationship.  This is a has-a relationship, where
# Child has-a Other that it uses to get its work done.  

# We can see that most of the code in Child and Other is the same to accomplish the same thing.  The only difference is that I had to define a 
# Child.implicit function to do that one action.  I could then ask myself if I need this Other to be a class, and I just make it into a module named other.py?

# When to use interitance or composition

# Inheritance vs Composition comes down toan attempt to solve the problem of reusable code.  You don't want to have duplicated code all over your code, 
# since that's not clean and efficient.  Inheritance solves this problem by creating a mechanism for you to have implied features in base classes. 
# Composition solves this by giving you modules and the ability to simply call functions in other classes.