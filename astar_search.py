"""A* search algorithm for HW 1 (8-puzzle A* search)."""

import Queue

import numpy

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def a_star(b, fcn):
	"""
	Runs A* algorithm to find optimal path from current to goal state.
	
	Parameters:
		b - Board - starting board state
		fcn - integer - which heuristic to use
	
	Returns:
		3-tuple: (cost, depth, effective branching factor)
	"""
	
	# Set of tuples: (f(n), g(n), h(n), Board).
	open_set = Queue.PriorityQueue()

	# Set of nodes already expanded.
	closed_set = set()
	
	h = None
	if fcn == 1: h = h1(b)
	elif fcn == 2: h = h2(b)
	else: h = h3(b)
	
	open_set.put((h, 0, h, b))
	
	depth = None
	
	done = False
	
	#print "GOING IN"
	
	cost = 1
	
	while not done:
		
		node = open_set.get()
		closed_set.add(node[3])

		#print len(closed_set)
		
		# Heuristic is 0, goal state found.
		if node[2] == 0:
			done = True
			depth = node[1]
			
		else:
			
			g = node[1] + 1
			#print "g is " + str(g)
			front = node[3].moves()
			
			for n in front:
				
				if n not in closed_set:
					cost += 1
					#if cost % 100 == 0:  print cost
						
					if fcn == 1: h = h1(n)
					elif fcn == 2: h = h2(n)
					else: h = h3(n)
				
					open_set.put((g+h, g, h, n))
			
			#print "got here!"
	
	return (cost, depth, branch_factor(cost, depth))

def h1(b):
	"""
	Heuristic function: returns number of misplaced tiles.
	
	Parameters:
		b - Board - board to analyze
		
	Returns:
		int - # of misplaced tiles
	"""
	
	misplaced = 0
	
	for i in range(0, 3):
		for j in range(0, 3):
			if b.board[i][j] != 0:
				if b.board[i][j] != 3*i + j:
					misplaced += 1
	
	return misplaced

def h2(b):
	"""
	Heuristic function: returns sum of distances from goal positions.
	
	Parameters:
		b - Board - board to analyze
		
	Returns:
		int - sum of distances from goal positions
	"""
	
	distance = 0
	
	for i in range(0, 3):
		for j in range(0, 3):

			# Find distance for all tiles except "0" tile.
			if b.board[i][j] != 0:
				distance += abs(i - b.board[i][j] / 3)
				distance += abs(j - b.board[i][j] % 3)
	
	return distance

def h3(b):
	"""
	Heuristic function: TBA
	
	Parameters:
		b - Board - board to analyze
		
	Returns:
		int - 
	"""

	lc_r = [0, 0, 0]
	lc_c = [0, 0, 0]
	
	for i in range(0, 3):
		
		c = [0, 0, 0]
		
		for j in range(0, 3):
			
			if b.board[i][j] != 0:
				
				for x in range(0, j):
					if b.board[i][x] != 0 and b.board[i][x] > b.board[i][j]:
						c[i] += 1
				
				for x in range(j+1, 3):
					if b.board[i][x] != 0 and b.board[i][x] < b.board[i][j]:
						c[i] += 1
		
		while c[0] != 0 or c[1] != 0 or c[2] != 0:
			
			k = 0
			if c[1] > c[k]: k = 1
			if c[2] > c[k]: k = 2
			
			c[k] = 0
			
			for x in range(0, k):
				if b.board[i][x] != 0 and b.board[i][x] > b.board[i][k]:
					c[x] -= 1
			
			for x in range(k+1, 3):
				if b.board[i][x] != 0 and b.board[i][x] < b.board[i][k]:
					c[x] -= 1
			
			lc_r[i] += 1
	
	for j in range(0, 3):
		
		c = [0, 0, 0]
		
		for i in range(0, 3):
			
			if b.board[i][j] != 0:
				
				for x in range(0, i):
					if b.board[x][j] != 0 and b.board[x][j] > b.board[i][j]:
						c[j] += 1
				
				for x in range(i+1, 3):
					if b.board[x][j] != 0 and b.board[x][j] < b.board[i][j]:
						c[j] += 1
		
		while c[0] != 0 or c[1] != 0 or c[2] != 0:
			
			k = 0
			if c[1] > c[k]: k = 1
			if c[2] > c[k]: k = 2
			
			c[k] = 0
			
			for x in range(0, k):
				if b.board[x][j] != 0 and b.board[x][j] > b.board[k][j]:
					c[x] -= 1
			
			for x in range(k+1, 3):
				if b.board[x][j] != 0 and b.board[x][j] < b.board[k][j]:
					c[x] -= 1
			
			lc_c[j] += 1
	
	l_conflict = 2 * (lc_r[0] + lc_r[1] + lc_r[2] + lc_c[0] + lc_c[1] + lc_c[2])
	
	return h2(b) + l_conflict

def branch_factor(cost, depth):
	"""
	Calculates the effective branching factor (b*).
	
	Parameters:
		cost - int - number of nodes expanded
		depth - int - depth of search
		
	Returns:
		float - effective branching factor, rounded to 2 places after the decimal
	"""

	# Create an array of coefficients for a polynomial equation.
	coeffs = []

	for i in range(depth):
		coeffs.append(1)

	coeffs.append( -1 * cost)

	# Solve for the roots of the equation.
	roots = numpy.roots(coeffs)

	# Choose the valid root and return it, rounded to 
	for comp in roots:
		if comp.imag == 0.0:
			return -1.0*round(comp.real, 2)
