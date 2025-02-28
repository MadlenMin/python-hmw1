
while True:
	try:
		user_input = int(input("type a number: "))
		if user_input == 0:
			break
		elif (user_input % 2) == 0:
			print("The number is even")
		else:
			print("The number is odd")
	except ValueError:
		print("Hmm this is not a number , try one more time : ")
			
		
