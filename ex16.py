# commands to remember:

# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file, you can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file, watch out if you care about the file.
# write(stuff) -- Writes stuff to the file.


from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL - C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# "w" means tro truncate the file to 0 length or create text file for writing.  
#This will wipe all of the contents in existing 
#check python argument modes here: http://stackoverflow.com/questions/1466000/python-open-built-in-function-difference-between-modes-a-a-w-w-and-r
target = open(filename, "w")

print "Truncating the file.  Goodbye!"
#target.truncate() and "w" are redundante since they serve the same purpose, but good to know either or exists.
target.truncate()


print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()






