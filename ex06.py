def is_palindrom(a):
	if a == a[:: - 1]:
		return("Yes !Your word is a palindrom")
	else:
		return("No ( it is not palindrom")
user_input = input("type a word : ")

print(is_palindrom(user_input))


		
		
