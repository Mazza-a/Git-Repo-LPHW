from sys import argv

#assigns two arguments to argv
script, filename = argv

#first prints a format string using our filename argument, then prints out a question for the raw_input
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."
raw_input("?")

#prints open file and then opens the file in write mode
print "Opening the file..."
target = open(filename, 'w')

#Truncates the file(deletes every thing in the file)
print "Truncating the file.   Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines"

#asks the user for three lines and stores them in separate variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write to the file."

#Writes what the user wrote from the 3 raw_inputs to the blank file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Closes the file after writing the text
print "And finally, we close it."
target.close()
