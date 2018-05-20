import math
import timeit

###############PROBLEM 10##############
#Summation of primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def SOP(n):
#after finding out that I only need check if a number is divisible by primes after a certain point...
	primes = [2,3,5,7]
	x = 11
	while x <= n:
		prime = True
		index = 0
		while primes[index] <= int(math.sqrt(x)+1):
			if x%primes[index] == 0:
				prime = False
			index += 1
		if prime == True:
			primes.append(x)
		x += 2
	return sum(primes)
		
#counter that was used to determine speed
def split1(n):
	s = []
	s.insert(0,SOP(11,10000))
	for n in range(1,(n//10000)):
		print(n)
		s.insert(0,SOP((10000*n)-1,10000*(n+1)))
	return sum(s)

#######################################