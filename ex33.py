# while-loop will keep executing the code block under it as long as a boolean expression is True.
# REMEMBER: if we write a line and end it with a : (colon) then that tells Python to start a new block of code.  Then we indent and that's the new code.

# while loops does a test like an if-statement, but instead of running the code block once, they jump back to the "top" where the while is, and repeat.  It keeps doing this until the expression is False.
# PROBLEM: sometimes they do not stop.  You almost always want your loops to end eventually.

# TO AVOID THIS PROBLEM: 
#	1. Make sure that you use while-loops sparingly.  Usually a for-loop is better.
#	2. Review your while statements and make sure that the thing you are testing will become False at some point.
#	3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.

# to kick start this while-loop, to start, we have NO numbers in the numbers bracket.
# i = 0 is to start.
i = 0
# as mentioned, there are no numbers defined in the bin "[]"
numbers = []
# while i < 6 meaning i will range anywhere from 0 to 5
while i < 6:
	# print the string and use the decimal formatter to represent the value of "i"
	print "At the top i is %d" % i
	# once the decimal formatter is defined for i, append this value to the i list.  meaning add this value as the last value to the list.
	numbers.append(i)

	# i = i + 1 also means we know what i is, now increase it by 1.
	# or it can also be i += 1
	i += 1
	print "Numbers now: ", numbers
	# print the string "Numbers now: ", and use the variable numbers which will show a bracket and the numbers in there
	print "At the bottom i is %d" % i
	# print the string "At the bottom i is %d" % i; meaning print this string with the decimal formatter.  i will be the result of i = i + 1 (or the incremented value)

print "The numbers: "
	# print this string "The numbers: "

for num in numbers:
	# setting num = numbers
	print num
	# call num and print the values that are now in the numbers bracket.