""" The following code prints questions and then prompts 
the user to answer the question and assigns it to a variable"""
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# Uses the values gathered by  the initial code and uses it to string format
print "so you're %r old, %r tall and %r heavy." % (age, height, weight)


