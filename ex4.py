# Defining all the variables I need to run my code
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpools_capacity = cars_driven * space_in_a_car 
average_passengers_per_car = passengers / cars_driven

# printing lines with the variables that i just defined
print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpools_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"

