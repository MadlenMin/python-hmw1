string = input("Type smthg: ")

listik = ['a','e','i','o','u','A','E','I','O','U']

length = len(string)

count = 0

for i in range(length):
	if string[i] in listik :
		count += 1
print(f"the number of vowels in this sentence is : {count} , just a question , Why do you need to know that ?")
	


