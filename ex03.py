def add(x,y):
	return (x + y)
def subtract (x,y):
	return (x - y)
def divide (x,y):
	if y == 0:
		return ("I can't divide by 0, try again")
	return(x/y)
def multiply (x,y):
	return x*y

while True:
	print(" Choos an action below by typing in the number")
	print(" 1 is +" , "\n", "2 is -", "\n","3 is /","\n","4 is *","\n", "5 is exit")
	
	try :
		num = int(input(" Your chois is ? : "))
		if num == 5:
			break

		if num == 1 or num == 2 or num == 3 or num == 4:
			try:
				nbr1 = int(input("Your first number is : "))
				nbr2 = int(input("Your second number is : "))
			
				if num == 1:
					print(add(nbr1,nbr2))
				elif num == 2:
					print(subtract(nbr1,nbr2))
				elif num == 3:
					print(divide(nbr1,nbr2))
				elif num == 4 :
					print(multiply(nbr1, nbr2))
			except ValueError:
				print("Error try again")
	except ValueError:
		print("Wrong choice , try again")
