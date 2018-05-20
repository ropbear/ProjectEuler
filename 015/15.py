import math
import timeit

###############PROBLEM 16##############
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?
def power(base,n):
	prod = 1
	t = 0
	while t < n:
		prod *= base
		t += 1
	ps = str(prod)
	sumlist = []
	for i in range(len(ps)):
		sumlist.append(int(ps[i]))
	return sum(sumlist)


#SHABAM; FLASHED IT!

#######################################
