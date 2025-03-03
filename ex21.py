def digit_count(nbr):
	count = 0
	if nbr == 0:
		return 1
	nbr = abs(nbr)
	while nbr > 0:
		nbr //= 10
		count += 1
	return count

def Armstrong(nbr):
	og = nbr
	power = digit_count(nbr)
	new_number = 0
	while nbr > 0:
		new_number += (nbr % 10)**power
		nbr //= 10
	if new_number == og:
		print("Your number is an Armstrong number")
	else:
		print("Your number is not Armstrong")

num = int(input("Write a number : "))
Armstrong(num)
