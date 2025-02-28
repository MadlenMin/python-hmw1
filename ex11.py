
a = ['a','e','i','o','u']

user_input = input("type smthg : ")

count = 0

for char in user_input:
	if char in a:
		count +=1
print("Number of vowels is : " ,count)
