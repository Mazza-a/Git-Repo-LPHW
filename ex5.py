# creating variables to put into my format string (%s, %) code
"""" The following information is based on the author of Learn
Python the Hard Way Zed A. Shaw """
my_name = "Zed A. Shaw" 
my_age = 35
my_height = 74 
my_weight = 180
my_eyes = "Blue"
my_hair = "Brown"
my_teeth = "white"

# printing each format string out individually with an exception 
print "let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Hos teeth are usually %s depending on the coffee" % my_teeth

# putting all of the number values into a format string on one line and printing
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight
, my_age + my_height + my_weight)
