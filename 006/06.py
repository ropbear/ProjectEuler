import math
import timeit

###############PROBLEM 7###############
#10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def primeID(n):
	found = False
	num = 0
	count = 0
	while found == False:
		if list_divisors(num) == [1]:
			count += 1
			if count == n:
				return num
		num += 1
		
# i can probalby make a better isPrime function than using list divisors...
#######################################
