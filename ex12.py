# very helpful pydoc documentation: http://docs.python.org/2/library/pydoc.html
# pydoc -p 1234 creates a documentation that can be viewd on localhost:1234
# pydoc os, open, file, or sys for more info


y = raw_input("Name? ")

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

print "So you're %r old, %r tall, and %r heavy." % (age, height, weight)

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

print "So you're %s old, %s tall, and %s heavy." % (age, height, weight)

# more info on why to use %r or %s  http://stackoverflow.com/questions/6005159/when-to-use-r-instead-of-s-in-python
# %r shows with quotes while %s just shows the string (with no quotes)


