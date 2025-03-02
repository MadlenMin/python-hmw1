nbr = int(input("Type a number : "))

num = 0

while nbr != 0:
	num += (nbr % 10)
	nbr //= 10
print(num)
