from sys import argv

# Sets 2 arguments to argv 
script, filename = argv

#sets txt variable to the open function which uses the filename argument as a parameter
txt = open(filename)

# Prints a format string using the filename argument 
print "Here's your file %r:" % filename

# Tells the file object that we called using open() and tells it to read the file with no parameters
print txt.read()

#the remaining code repeats the same code but instead uses raw_input to open the file
print "Type the filename again"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

