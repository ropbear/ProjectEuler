import math
import timeit

###############PROBLEM 1###############
#Multiples of 3 and 5

def multsTF(n):
	mults = []
	for num in range(n):
		if num%3 == 0 or num%5 == 0:
			mults.append(num)
	summ = 0
	for x in mults:
		summ += int(x)
	return summ

#######################################