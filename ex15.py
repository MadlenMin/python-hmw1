listik = input("Enter numbers: ").split()

listik2 = list(map(int, listik))

length = len(listik2)
sum = 0

for i in range(length):
	sum += listik2[i]
print(f"You relly could not do the sum ? {sum} You'r welcom , go buy a calculator")
 

