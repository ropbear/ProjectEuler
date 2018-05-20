import math
import timeit

###############PROBLEM 9###############
#Special Pythagorean Triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def SPT(n):
	trips = [1,1,1]
	while trips[0] != n/2:
		if (trips[0]*trips[0])+(trips[1]*trips[1]) == trips[2]*trips[2]:
			if trips[0]+trips[1]+trips[2] == n:
				return trips[0]*trips[1]*trips[2]
#this is kind of ugly... it's a good ticker though, kind of like a clock. Also very slow when n >>> 1 so that is why I use n/2, which assumes the largest triplet number is < n/2
		if trips[2] < n/2:
			trips[2] += 1
		elif trips[2] == n/2:
			trips[2] = 1
			if trips[1] < n/2:
				trips[1] += 1
			elif trips[1] == n/2:
				trips [1] = 1
				if trips[0] < n/2:
					trips[0] += 1
#######################################