def multy_table(a):
	count = 1
	while count <= 10:
		result = count * a
		print(f"{count} X {a} = {result}")
		count += 1
nbr = int(input("enter your number : "))

multy_table(nbr)
