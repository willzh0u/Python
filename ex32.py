the_count = [1, 2, 3, 4, 5,]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
values = [6, 7, 8, 9, 10, 11]


# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one 
elements = []
numbers = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i


for x in range(6, 11):
	print "We are now using the bigger numbers like %d in the list." % x
	elements.append(x)

# notice for x in range(6, 11): only loops 5 times for 6, 7, 8, 9, and 10, but no 11.  
# The range() function only does numbers from the first to the last, not including the last.
# So it stops at 10 and 11 in the above.  This turns out to be the most common way to do this kind of loop.

for x in elements:
	print "Number was: %d" % x


	# what does elements.append() do?
	# it simply appends to the end of the list.  
	# in my example, I added "numbers" after "elements." I appended 6-10 to elements which was just 1-5.
	# as you can see, line 39, I wanted to print the list of numbers in elements and it NOW prints 0-10.