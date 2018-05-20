import math
import timeit

###############PROBLEM 15##############
#Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner. 
#How many routes for a 20 by 20 grid?
def grid(n):
	n += 2
	g = [[0]*n]*n
	n -= 1
	g[n-1][n] = 1
	g[n][n-1] = 1
	for x in range(n):
		for y in range(n):
			g[(n-2)-x][(n-2)-y] = g[(n-1)-x][(n-2)-y]+g[(n-2)-x][(n-1)-y]
	return g[0][0]

#dealing with n is really messy here because of the difference between the way it was solved and user friendliness. Also an easy fix for index out of range

#######################################
