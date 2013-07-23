# from sys module, argv is a feature
from sys import argv

# argument value 
script, input_file = argv

# define function print_all with variable (f)
def print_all(f):
#print variable f and read what it is
	print f.read()
# define function rewind with f variable
def rewind(f):
# seek() method sets the file's position.    The whence argument is optional and defaults to 0
# which means absolute file positioning, other values are 1 which means seek relative to the current
# position and 2 means seek relative to the file's end.
	f.seek(0)
# define function print_a_line with variables (line_count & f)
def print_a_line(line_count, f):
# print what line_count is and f_readline() is a method that reads one entire line from the file "f".
# HOW DOES REDLINE know where each line is? - inside readline is code that scans each byte
# of the file until it finds a \n character, then stops reading the file to return what it found so far  
# the file f is responsible for maintaining the current position in the file after each readline() call, 
# so that it will keep reading each line.
	print line_count, f.readline()
# current_file is a variable and it equals input_file (opened).  
#input file is the filename you will be opening with this script.
current_file = open(input_file)
# prints the below string and breaks a line after due to "\n"
print "First let's print the whole file:\n"
#current_file is the variable within print_all function
print_all(current_file)
# just a pring string
print "Now let's rewind, kind of like a tape."
# rewind function with current_file as variable
rewind(current_file)
# prints string
print "Let's print three lines:"
# After lines are printed, it's auto broken with a space between each line
# because the readline() function retunrs the \n that's in the file at the end of that line.
# This means that print's \n is being added to the one already returned by readline().
# IF YOU DON'T LIKE THE SPACING, JUST SIMPLY ADD A COMA (,) AT THE END.
current_line = 1
print_a_line(current_line, current_file)
# += is similar to "it is as it's" and "you are as you're".  It's just a contraction
# and this kind of like a contraction for the 2 operations = and +.  
# this also means x= x + y is same as x += y
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)





