
numbers = []
user_input = 0

while user_input != 2:
	user_input = int(input('choos 1 or 2 \n'))
	if user_input == 2:
		break
	elif user_input == 1:
		numbers.append(int(input("Write a number \n")))
	else:
		print("nope honey choos 1 or 2")

print('\n',sum(numbers))
#what to do in case of invalid input ?

	

