number = input("Give me 3 numbers : ").split()

listik = list( map(int, number))
 
length = len(listik)

max = 0

for i in range(length):
	if listik[i] > max:
		max = listik[i]
print(max)
