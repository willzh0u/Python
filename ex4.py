cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", cars_not_driven, "empty cars today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "My example"
#remember answer is represented by PEMDAS computation format
print cars + drivers * passengers


#Study Drills
#4.0 is floating point.  Decimal fixed point verus floating point.  The use of decimal floating point eliminates decimal representation error (making it possible to represent 0.1 exactly); how ever, sopme operations can still incur round-off error when non-zero digits exceed the fixed precision.
#floating point numbers are represented in computers as base 2 fractions.  For example, the decimal fraction 0.125 is a floating-point.  A value of a fixed-point data type is essentially an integer that is scaled by a specific factor determined by the type. For example, the value 1.23 can be represented as 1230 in a fixed-point data type with scaling factor of 1/1000, and the value 1230000 can be represented as 1230 with a scaling factor of 1000. Unlike floating-point data types, the scaling factor is the same for all values of the same type, and does not change during the entire computation.
#
#
#
#
#
#