import math
import timeit

###############PROBLEM 12##############
#What is the value of the first triangle number to have over five hundred divisors?

def triangles(div):
	summ = 0	
	num = 1
	while True:
		summ += num
		if summ%2 == 0:
			dlist = list_divisors(summ)
			if len(dlist)*2 >= div:
				return summ
		num += 1
		

#######################################
