# people, cars, and buses are defined variables.  In the examples below, we have if/elif/else statements.
# the elif statement is sort of like a branched answer.  If not this, then that.  elif is the "then that".  
# you can have multiple elifcs in an if statement, but the function stops after the first elif is true.

people = 30
cars = 40
buses = 15
# if cars is greater than people, print "we should take cars"
# or if cars is less than people, print "we should not take cars"
# if cars = people, that will fall into the "else" line where it will print "we can't decide"
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."





# the elif statement allows you to check multiple expressions for truth value and execute a block of code as soon as one of the conditions evaluate to true.
# else is the "other" alternative "branch" to your code.
# if multiple elif blocks are true; Python starts at the top and runs the first block that is True, so it will run only the first one.
