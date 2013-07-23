# Animal is-a object (yes, sort of confusing) look at the extra credit)
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init(self, name):
		## is-a
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## is-a
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee is-a Person hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass
## Salmon is-a Fish
class Salmon(Fish):
	pass
## Halibut is-a Fish
class Halibut(Fish):
	pass
# Rover is-a Dog
class Rover(Dog):
	pass
## satan is-a cat
satan = Cat("Satan")
## mary is-a person
mary = Person("Mary")
## mary has-a pet
mary.pet = satan
## frank is-a Employee
frank = Employee("Frank", 120000)
## flipper is-a fish
flipper = Fish()
## crouse is-a salmon
crouse = Salmon()
## Harry is-a halibut
harry = Halibut()



# YOU CAN FIND MORE INFO HERE: https://github.com/kingnez/learn-python-the-hard-way/blob/master/ex42.py

# class - tell Python to make a new king of thing. Salmon is a type of Fish; it's a class of Fish
# object - Two meanings: the most basic kind of thing and any instance of something. Mary is the name of a Fish.  It's an object.  Ex 42!  Object is a class of a class ClassName(object):
# class is a object -A class inherits from the class named object to make a class but it's not an object reallt it's a class, but do not forget to inherit from object.

# Study Drills
# 1. There is a "Class is a object" weird class, because it hsa a number of immediate benefits, like the ability
#	 to subclass most built-in types, or the introduction of "deciptors", which enable computed properties. 
# 2. How to use class like it's an Object (http://docs.python.org/2/tutorial/classes.html): 

#	class MyClass:
#		"""A simple example class"""
#		i = 12345
#		def f(self):
#			return 'hello world'

# *note: __init__() is a method 
# 3. 

# FAQ2: WHAT IS THE POINT OF SELF.PET = None?
#	That makes sure that the self.pet attribute of that class is set to a default of None.

# FAQ3: What does super(Employee, self).__init__(name) do?
#	That's how you can run the __init__ method of a parent class reliably.  Go search for "python super" and read the various advice on it being evil and good for you.

# Python Super() = http://stackoverflow.com/questions/576169/understanding-python-super-and-init-methods
# 
# Example

# class Child(SomeBaseClass):
# 	def __init__(self):
# 		super(Child, self).__init__()

# #versus this

# class Child(SomeBaseClass):
# 	def __init__(self):
# 		SomeBaseClass.__init__(self)

# The benefits of super() in single-inheritance are minimal.  Mostly, you don't have to hard code the name of the base class into every method that uses its parents methods.  
# However, it's almost impossible to use multiple-inheritance without super().  This extends to code that later exttends yours.  If somebody later wanted to write a class that extended Child and a mixin, their code would not work properly.
		