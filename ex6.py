# Assigning the values to variables im going to use
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)
# printing the value of x with the format string value of 10
print x 
# printing the value of y with the format string values of binary and do_not which contain the string values "binary" and "dont"
print y
#printing a string with the format string value of my y value
print "I said: '%s'." % y
# assigning values for my next format string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 
# format string with two values one containing a string the other the value which is a False boolean
print joke_evaluation % hilarious
# variables containing strings so I can add them together easily
w = "This is the left side of..."
e = "a string with a right side"

print w + e
