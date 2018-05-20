###############PROBLEM 14##############
#Using the rule n-> n/2 (n is even) and n-> 3n+1 (n is odd), which starting number (n0) under one million produces the longest chain,
#assuming every number goes to 1 with this sequence? (Collatz Problem)

def collatz(n):
	count = 0
	while n>1:
		if n%2 == 0:
			n /= 2
		elif n%2 != 0:
			n = (3*n)+1
		count += 1
	return count

def lcollatz(mahx):
	count = [0,0]
	while mahx != 0:
		temp = collatz(mahx)
		if count[0] < temp:
			count[0] = temp
			count[1] = mahx
		mahx -= 1
	return count[1]
	
#######################################