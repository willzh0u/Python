from sys import argv

script, user_name, smart = argv
prompt = '>'

print "Hi %s, I'm the %s script.  Are you %s" % (user_name, script, smart)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Are you smart, %s?" % user_name
intelligence = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me. You are %r smart.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, intelligence, lives, computer)


# Zork and Adventures is one of the earliest interactive fiction computer games.
# QUESTION - for someone new running an argv script (like this one), how do they tell how many "values" are needed to unpack?