from sys import argv

# Sets two arguments to argv
script, user_name = argv

#sets variable prompt to '>'
prompt = 'ENTER:'

# prints a format string that takes the arguments we set for argv
print "Hi %s I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."

#prints a format string that takes the user_name argument we set for argv
print "Do you like me %s?" % user_name

#sets the variable likes to the input of the user after '>'
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)

#prints a format string with values taken from  the users answered questions
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And You have a %r computer. Nice.
""" % (likes, lives, computer)