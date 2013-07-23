print "I am 6'2\" tall." #escape double-quote inside string
print 'I am 6\'2" tall.' # escape single-quote inside string


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
test_cat = "I'm a \ntest tab cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat2 = '''
I'll do a list2:
\t* Cat food
\t* Fishies
\t* Catnip\n\t\v\v* Grass\f*Carrots
'''

Cat_Study_Drills = "I don't like cats that are %s'2\" feet wide" % 2.34
Cat_Study_Drills_2 = 'I don\'t like cats that are %s\'2" feet wide' % 2.23

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print test_cat
print fat_cat2
print Cat_Study_Drills	
print Cat_Study_Drills_2




while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,

