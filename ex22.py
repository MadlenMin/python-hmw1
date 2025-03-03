def second_max(b):
	first = max(b)
	second = min(b)
	for i in range(len(b)):
		if b[i] > second and b[i] < first:
			second = b[i]
	print(f"Your second largest number is {second}")
	
		
a = [ 1,3,4,78,2,18,44,42]
second_max(a)




