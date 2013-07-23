
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)

#raw_input does not exist in Python 3.x while input() does.  raw_input() returns a string, and input() tries to run the input as a Python expression.  
# Since getting a string was almost always what you wanted, then use int(raw_input()) to get a string back.
# do NOT use eval(raw_input()), because you need to type answers in quotes like "1" and you don't want '"1"' in quotes as the answer.  You only want the number 1.
# http://mail.python.org/pipermail/tutor/2001-February/003494.html



print "How many meals do you eat a day?",
eat = int(raw_input())
print "How many times do you brush your teeth a day?",
brush = int(raw_input())

print "So you eat %r meals and brush %r times a day." % (eat, brush) 



print "type anything"
x = int(raw_input())
