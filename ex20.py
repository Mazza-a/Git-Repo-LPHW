from sys import argv

# sets 2 arguments for argv
script, input_file = argv

#defines a function that takes one argument which reads the file passed through it and prints the data
def print_all(f):
	print f.read()

#defines a function that takes one argument and when a file is passed through it opens the file moves to the first word and starts reading the file
def rewind(f):
	f.seek(0)

#defines a function that takes two arguments that prints the line the file is reading and prints that line
def print_a_line(line_count, f):
	print line_count, f.readline()

#sets a variable to open a file using an argument set at the beginning of the code to argv
current_file = open(input_file)

print "First let's print the whole file:\n"

#prints the file that was opened
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#uses rewind function to seek all the way back to the beginning of the file
rewind(current_file)

print "let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)