# this is a module.  to run ex25.py, we will do the following.
# 1. type Python
# 2. type import ex25 (you don't need the .py)
#3 make sentence = anything so you can run your function against it.

# We use the ex25 module and call our first function ex25.break_words.  The. (dot,period) symbol
# is how we tell python "Hey, inside ex25, there's a function called break_words and I want to run it."

# after we print words esp the first and last, those words are now missing.

# instead of typing python, then import ex25, we can also say "ex25 import *" to import everything from ex25.

# what is .pop(0) below? - .pop(0) remove the item at the given position in the list, and return it.
# If no position or index is specificed, a.pop() removes and returns the last item in the list.  

# after you've printed every word in the sentence, the script will return an IndexError: pop from empty list.

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""PRints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


	# RECAP OF WHAT HAPPENED IN EX25

	# instead of running this exercise like we did before, we went into python first.  Then import ex25 (no.py at end)
	# ex25 contains all the functions we'll be using and we'll use the python interpretor to help us run diff functions.
	# we first declared a variable sentence = "All good things come to those who wait."
	# we then declared words = ex25.break_words(sentence) <-- remember, sentence is just a variable that gets plugged into where "stuff" is in the break_words function.
	# type words and it will run the break_words function on the "sentence" variable.
	# next, we declared sorted_words = ex25.sorted_words(words), calling the sorted_words function on the "words" variable.  This will sort the sentence into alphabetical order.
	# sorted words will print the list of words in alphabetical order.
	# next, ex25.print_first_word(words) calls the function print_first_word on the "words" variable.  remember, words = break_words from "sentence"!
	# next, ex25.print_last_word(words) does the same but on the last variable.
	# Important; when first and last words are called already, they are sort of taken out of the sentence.  You will next call "sorted_words" and you will notice it's missing first & last words.
	# next, you will set sorted_words = ex25.sort_sentence(sentence).  you are setting "sorted_words" = to the outcome of the sort_sentence function called on "sentence".  This will sort of start fresh on a brand new "sentence" again.  Here you will sort the entire "new" sentence all over again.
	# next, you will enter "sorted_words" and will notice the entire sentence shows again in a sorted alphabetical order.
	# next, you will call the function print_first_and_last on the "sentence" variable.  It will print the first and last words of "sentence"
	# next, you will call the "print_first_and_last_sorted" function on sentence.  This will print the first and last words of "sentence" from the SORTED order!
	# NOW YOU'RE DONE WITH EX. 25!





	
