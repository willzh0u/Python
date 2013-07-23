#NOTE: there are lots of commented code here.  please read carefully before running script


from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# when I commented the third variable line:
# Traceback (most recent call last):
  # File "ex13.py", line 3, in <module>
    # script, first, second, third = argv
# ValueError: need more than 3 values to unpack

# With 4 arguments
script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

# to test the print summary
#print "So here is %r script, %r first, %r second, %r third, %r fourth." % (script, first, second, third, fourth)



# combine raw_input with argv to make a script that gets more input from a user.

# What's the difference between argv and raw_input()?
# The different has to do with where the user is required to give input. 
# If they give your script inputs on the command line, then you use argv. If you want them to input using the keyboard while the script is running, then use raw_input().


## argv tends to ask you for inputs before hand "ie. python ex13.py first second" and then it spits everything out.
## raw_input on the other hand asks you to type in the answer to each question and spits out a summary sentence.
## see https://github.com/knockycode/LearningPython/blob/master/ex13_ec.py

script, age, height = argv

print "The name of the script:", script
print "The name of how old you are:", age
print "The name of how tall you are:", height


age = raw_input("How old are you?")
height = raw_input("How tall are you?")

print "So you are %r years old and %r." % (age, height)







