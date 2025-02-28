import random

a = random.randint(0,10)

tris = 0

while True:

	try:

		user_input = int(input("Guess the number "))
		if user_input > a :
			tris += 1
			print("Too high")
		elif user_input < a:
			tris += 1
			print("Too low")
		elif user_input == a:
			print ("You are right!!! the number is : " , a)
			print("You did :", tris , "attampts")
			break
	except ValueError:
		print("Nope not a valid input try again with a number")

		

