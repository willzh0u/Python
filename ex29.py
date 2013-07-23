people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats!  The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

dogs += 5
# with dogs incremented by 5, people = dogs
if people >= dogs:
	print "People are greater than or equal to dogs."
# with dogs incremented by 5, people = dogs
if people <= dogs:
	print "People are less than or equal to dogs."
# with dogs incremented by 5, people = dogs
if people  == dogs:
	print "People are dogs."

# lines 29-32 added for Study Drill #4.
if people < cats:
	print "Not so cool."
else:
	print "Actually that's fine."

#1. if is conditional that can provide 1 of 2 (possibly more) answers.  If this do that, if not, do this instead.
#1. - from ex30 - The if statement tells your script, "If this boolean expression is True, then run the code under it, otherwise skip it."
#2. You need to indent code, because it's a code block.  This means that whitespace is significant, and must be consistent.  If statements are a type of code block.
#2. - from ex 30 - A colon ":" at the end of a line is how you tell Python you are going to create a new "block" of code, and then indenting 4 spaces tells Python what lines of code are in that block.
#3. The code will return an Indentation Error: expected an indented block.
#3. - from ex 30 - If it isn't indented, you will most likely create a Python error. 
#4. Added on lines 29-32
#5. Doesn't matter if you change the variables.  Variables can be anything.  It only matters if you change the numbers.


# what does += mean?  The code x += 1 is the same as doing x = x + 1 but involves less typing.  
# You can call this the "increment by" operator.  Same goes for -= and many other expressions.