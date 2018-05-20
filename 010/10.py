import math
import timeit

###############PROBLEM 11##############
#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

def gridProd():
	grid = open('problem11.txt','r')
	matrix = []
	for line in grid:
		matrix.append(line.split())
	grid.close()

	print(int(matrix[6][8])*int(matrix[7][9])*int(matrix[8][10])*int(matrix[9][11]))
	maxmul = 0
	for y in range(0,20):
		for x in range(0,20):
			if x < 17 and y < 17:
				right = int(matrix[y][x])*int(matrix[y][x+1])*int(matrix[y][x+2])*int(matrix[y][x+3])
				down = int(matrix[y][x])*int(matrix[y+1][x])*int(matrix[y+2][x])*int(matrix[y+3][x])
				adj = int(matrix[y][x])*int(matrix[y+1][x+1])*int(matrix[y+2][x+2])*int(matrix[y+3][x+3])
			adj2 = 0
			if x > 2 and y < 17:
				adj2 = int(matrix[y][x])*int(matrix[y+1][x-1])*int(matrix[y+2][x-2])*int(matrix[y+3][x-3])
			if maxmul < max(right,down,adj,adj2):
				maxmul = max(right,down,adj,adj2)
	return maxmul
#######################################
