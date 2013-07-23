# Speaking OOP

# Word Drills
#	class: Tell Python to make a new kind of thing.
#	object: Two meanings: the most basic kind of thing, and any instance of some thing.
#	instance: what you get when you tell Python to create a class
#	def: How you define a function inside a class.
#	self: Inside the functions in a class, self is a variable for the instance/object being accessed.
#	inheritance: The concept that one class can inherit traits from another class, much like you and your parents.
#	composition: The concept that a class can be composed of other classes as parts, much like how a car has wheels.
#	attribute:	A propterty classes have that are from composition and are usually variables.
#	is-a: A phrase to say that something inherits from another, as in a Salmon is-a Fish
# 	has-a: A phrase to say that something is composed of things or has a trait, as in a Salmon has-a mouth


# Phase Drills

# 	class X(Y)
		# "Make a class named X that is-a Y."

#	class X(object): def __init__(self, J)
		# "class X has-a __init__ that takes self and J parameters."

#	class X(object): def M(self, J)
		# "class X has-a function named M that takes self and J parameters."

#	foo = X()
		# "Set foo to an instance of class X."

#	foo.M(J)
		# "From foo get the M function, and call it with prameters self, J."

#	foo.K = Q
		# "From foo get the K attribute and set it to Q."



# A Reading Test

import random
from urllib import urlopen
# urllib.urlopen opens a network object denoted by a URL for reading.  If the URL doesnot have a scheme identifier, or if it has file: as its identifier, this opens a local file;
# otherwise it opens a socket to a server somewhere on teh network.  If the connection can be made the ioerror exception is raised.  If all went well, a file-like object is returned.
# more on urllib: http://docs.python.org/2/library/urllib.html
#
# example
#
# http_proxy="http://www.someproxy.com:3128"
# export http_proxy
# python
# ...
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class ###(###):":
		"Make a class named ### that is-a ###.",
	"class ###(object):\n\tdef __init__(self, ***)" :
		"class ### has-a __init__ that takes self and *** parameters.",
	"class ###(object):\n\tdef ***(self, @@@)":
		"class ### has-a function named *** that takes self and @@@ parameters.",
	"*** = ###()":
		"Set *** to an instance of class ###.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
					random.sample(WORDS, snippet.count("###"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		# fake class names
		for word in class_names:
			result = result.replace("***", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print question

			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"
