name = 'ZED A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # in cm
height2 = 74 # inches
weight = 180 * 0.453592 # in kilos
weight2 = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %s cm tall." % height
print "He's %d kilo heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %r, and %d I get %r." % (age, height, weight, age + height + weight)