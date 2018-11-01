def password()
	"""			
	This is a simple guess the password example program counting the tryouts of guessing the right word
	Requires: Guessing word (str)
	Ensures: Congratulation Advice when guessed
	"""
	p = "IlovePython"
	x = ""
	count=0
	while x != p:
		x = input("Password: ")
		print(count)
		count=count+1
		print ("Congratulations, the password is right!")
	return count
