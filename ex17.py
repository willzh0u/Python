#this program will help copy one file to another

from sys import argv
from os.path import exists

script, from_file, to_file = argv



# we could dothese two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)	

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# although files are closed when a program exits (which is why it still worked when you commented out those lines), 
#it's good practice to close files that you are finished with. as if this was a function and was called by some other function and you didn't close the files,
# it would leak file descriptors and after awhile the program would run out of them

# In this case it will work the same 99.9% of the time because when your 
# program closes Python will kill all the file objects that you created 
# and in the process the files will get written to the disk. However, to 
# understand why you need to call close() in the general case you need to 
# understand that when you do a write to a file the OS does not 
# immediately write the data to the disk (it would be too slow). Instead 
# it writes it to a holding area in memory (called a buffer) and then, 
# every so often, it copies the buffer out to the real file. When you call 
# close() one of the things that happens is that the buffer gets told to 
# write to disk, even if it's not full yet. If you don't call close you 
# can wind up with data missing from the end of your files.





