# Defines a function with two argument
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# prints a string format that uses one of the arguments as the value
	print "You have %d cheeses!" % cheese_count
	# same thing done on this line as done on the previous with the other argument
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#prints two strings and starts a new line after the second
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

#prints a string and runs the function with the values of the arguments set to 20 and 30
print "We can just give the function numbers directly:"  
cheese_and_crackers(20,30)

#prints a string then assigns variables with values 10 and 50
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#runs the function using the variables set to the values of 10 and 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#prints a string and then assigns the values of the functions arguments of 10 + 20 and 10 + 6
print "We can even do maths inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#prints a string and uses the variables previously set and maths to assign values to the functions arguments
print "And we can combine the two, variables and maths:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

