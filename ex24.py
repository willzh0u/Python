# this is a review of everything

# here we learned about \' which is a single quote escape in a double quote string
# we also learned about \\ which created 1 \ in the actual print.
# we also learned about \n which starts the following part of the string (existing and new strings) on a new line.
# we also learned about \t which tabs or indents the line.
print "Let's practice everything."
print "You\' d need to know \' bout escapes with \\ that do \n newlines and \t tabs."


# here we used """ 3 quotes to create a new line.  it's similar to \n
#\t indents the poem.  ALSO - YOU CAN'T COMMENT WITHIN THE POEM!
# ending the poem with """ also creates a line break to the next section of stuff
# \n breaks "the needs of love" on to the next line.
# \n\t\t = breaks onto next line and indents twice!

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# prints a long line

print "_________________"
print poem
print "_________________"

# five (the variable) = the mathematics of 10 - 2 + 3 - 6
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# defining the function secret_formula with variable started.
# we can also look at the below math as started = starting_point.
# meaning... jelly_beans = 10000 * 500 = 5000000.  jars = jelly_beans / 1000 so 5000000 / 1000 = 5000.
# then crates = jars / 100 so 5000 / 100 = 50.  

# remember, started is just a "temporary" variable inside the function secret_formula.  
# same with jelly_beans.

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
