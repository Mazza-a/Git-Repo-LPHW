print "You enter a dark room with two doors. Do you go through door #1, door #2, door #3 or #4?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating cheese cake. what do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your leg off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries"
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good Job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good Job!"
elif door == "3":
	print "You stumble into a 'wonderful' land filled with rainbows and JellyBabies"
	print "1. Eat a JellyBaby"
	print "2. Follow a kind pixie through a candy cane forest"
	print "3. Go back through the door you came in"
	
	fairy_land = raw_input("> ")
	
	if fairy_land == "1":
		print "The rest of the JellyBabies come to life angry and eat you. Good Job!"
	elif fairy_land == "2":
		print "The pixie leads you into a trap you become trapped in the forest and become a slave to the pixie empire. Good Job!"
	elif fairy_land == "3":
		print "You survive the horrors of Fairy Land. Good Job"
	else:
		print "A giant pigeon picks you up and feeds you to her children. Good Job!"
		
elif door == "4":
	print """You enter a dark room where a voice asks you "what is 1 + 1?" what do you answer?"""
	print "1. answer with '1'"
	print "2. answer with '2'"
	print "3. answer with '52'"
	
	answer = raw_input("> ")
	
	if answer == "1" or answer == "3":
		print "You feel a sharp pain in your chest, the voice has stabbed you in the heart you bleed out and die. Good Job!"
	elif answer == "2":
		print """The voice replies "Congratulations you've been accepted into the College of Prestigious Scholars." """
	else:
		print "For the ridiculousness of your answer death comes painfully and slowly. Good Job!"
else:
	print "You stumble around and fall on a knife and die. Good Job!"
	
	
	
	
