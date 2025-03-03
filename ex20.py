def gcd(a,b):
	c = max(a,b)
	while c > 0:
		if a % c == 0 and b % c == 0 :
			return c
		c -= 1
print(gcd(100,572))
			 
		
