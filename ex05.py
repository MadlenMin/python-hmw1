def factorial(n):

	if (n == 1 or n == 0):
		return (1)
	else:
		return(n * factorial(n - 1))

nbr = 10
print("your number is : " ,nbr, "\n" , "the factorial is " , factorial(nbr))

