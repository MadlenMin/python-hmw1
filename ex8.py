nbr = int(input("Type a number : "))

if nbr > 1:

	for i in range(2,(nbr//2)):
		if((nbr % i)== 0):
			print(f"{nbr} is not a prime number")
			break
	else:
		print(f"{nbr} is a prim number")
