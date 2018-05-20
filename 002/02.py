import math
import timeit

###############PROBLEM 3###############
#Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def list_divisors(n): #this can be improved upon, it's super slow dealing with ints that have 9 digits or more
	dlist = []
	for d in range(1,int(math.sqrt(n))+1):
		if n%d == 0:
			dlist.append(d)
	return dlist

def gen_primes(limit):
	plist = []
	for n in range(limit):
		if list_divisors(n) == [1]:
			plist.append(n)
	return plist

def LPF(n):
	l = len(str(n))
	digits = l//3
	plist = gen_primes(int(math.pow(10,digits)))
	plist.reverse()
	for num in plist:
		if n%num == 0:
			return num

#######################################