
# imports the argv from the sys module
from sys import argv

# only 1 value needed to run this scrip in argv; just need a filename.  NOTE: filename MUST exist or this script errors out
script, filename = argv
# open(filename) opens the filename you wish to see
txt = open(filename)
# string to return the raw representation of filename  
print "Here's your file %r:" % filename
# following up from above txt = opens the filename.  giving the ".read()" command says READ what txt is with no parameters.
print txt.read()
# this was added as part of extra credit to close the file after it's read.
print txt.close()
# string to print
print "Type the filename again:"
# following the question above, ">" is the prompt value asking for the raw_input of "Type the filename again:"
file_again = raw_input("> ")
# a little bit of substitution here.  txt_again is a new value defined by the output of open(file_again) which is defined by the input from the above raw_input value
txt_again = open(file_again)
# pretty much tells the computer to read what text_again is, which is defined by open(file_again), which is then defined by the input value from the raw_input.
print txt_again.read()
# this was added as part of extra credit to close the file after it's read.
print txt_again.close()

#using argv and indicating the filename.txt at hand in the command line can be quicker.
# using raw_input can be easier to understand in the way of question first, then answer second.  whereas argv is question & answer together in command line.