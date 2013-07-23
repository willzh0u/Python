
# x is a variable to a string.  %d is pretty much 10.  %d means signed integer decimal.
x = "There are %d types of people." % 10
# binary = binary; nothing fancy
binary = "binary"
# ditto to binary
do_not = "don't"
# y is a variable to a string.  %s is pretty much (binary and do_not) that is defined literally as (binary and don't).  %s is a formatter for string
y = "Those who know %s and those who %s." % (binary, do_not)


print x
print y

# this is a variable within a string that gets printed.  %s  = string(); converts any Python object using str().
print "I said: %r." % x
# same as above
print "I also said: '%s'." % y

# variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# just prints what those 2 variables are.
print joke_evaluation % hilarious


# variable
w = "This is the left side of..."
# variable
e = "a string with a right side."
# prints what w and e strings are.
print w + e