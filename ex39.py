
# ***PART 1***


# stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
# stuff['city'] = "San francisco"
# stuff[1] = "Wow"
# stuff[2] = "Neato"

# print stuff

# output = {'city': 'San francisco', 2: 'Neato', 'name': 'Zed', 1: 'Wow', 'age': 36, 'height': 74}
# why is the output in this order?

# ***PART 2***

# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI',
	# 'Oh my God': 'OMG'
}

# create a basic set of states and some cities in them
cities= {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '_' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']


# print some states
print '_' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city abbreviation
print '_' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
			state, abbrev, cities[abbrev])

print '_' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)
state2 = states.get('Iowa', None)

if not state: 
	print "Sorry, no Texas."

if not state2: 
	print "Sorry, no Iowa"

# get a city with a defauly value
city = cities.get('IO', 'Does Not Exist bro')
city = cities.get('TX', 'Does Not Exist')

print "The city for the state 'TX' is: %s" % city
print "The city for the state 'IO' is: %s" % city




# What can't we do with Dictionarys?

# Difference between lists and dictionary
# 	use lists for preset index values like 0 =; 1 =; 2 =; etc.  Use Dictionaries if you want to use additional values in your function.
#	A list is for an ordered list of items.  A dictionary is for matching some items (called "keys") to other items (called "values").

# what would I use dictionary for?
#	User Dictionaries if you want to store more information using something other than the preset index values of 0, 1, 2, and so on!
#	Anytime you have to take one value, and look up another value.  In fact you could call dictionaries look up tables (like a spreadsheet).

# what would I use a list for?
# 	A Python list is just a sequence of pieces of information.  You can use lists to store strings, numbres, and more!
#	A list is for any sequence of things that need to go in order, and you only need to look them up by a numeric index.

# What can't we do in Dict?
#	We can't declare things like age_list[0] = 19, because it wil result in a runtime error unless there is already and element 0.
#	However, if you have age_list=[0,0,0,0], then age_list[0] = 19 will work.
#	Reference: http://www.i-programmer.info/programming/python/3990-the-python-dictionary.html

# what if I need a dictionary but I need it to be in order?
#	Take a look at the collections.OrderedDict data structure in Python.  
#	In Python, the widely used built in dict type does not specify an order for the key/value pairs stored.
#	This makes it hard to use dictionaries as data storage for some specific use cases.
#
#	Example http://www.python.org/dev/peps/pep-0372/
#	
#	>>> d = OrderedDict()
#	>>> d['parrot'] = 'dead'
#	>>> d['penguin'] = 'exploded'
#	>>> d.items()
#	[('parrot', 'dead'), ('penguin', 'exploded')]


# Dict vs List vs Set
# http://stackoverflow.com/questions/513882/python-list-vs-dict-for-look-up-table dict is faster than all.
# http://www.codecademy.com/courses/python-beginner-en-pwmb1
# great examples: http://forum.codecall.net/topic/56851-dictionaries-in-pythonbeginers-tutorial/
