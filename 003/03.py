import math
import timeit

###############PROBLEM 4###############
#Largest Palindrome Product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def FLP():
	pal = 0
	for num1 in range(999,99,-1):
		for num2 in range(999,99,-1):
			prod = num1*num2
			sprod = str(prod)
			l = len(sprod)
			m = l//2
			low = sprod[:m]
			high = sprod[m:]
			revhigh = ''
			for index in range(len(high)):
				revhigh += high[-(index+1)]
			if low == revhigh and prod > pal:
				pal = prod
	return pal

#######################################