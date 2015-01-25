"""A* search algorithm for HW 1 (8-puzzle A* search)."""

import board

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"


def h1(b):
	"""
	Heuristic function: returns number of misplaced tiles.
	
	Parameters:
		Board to analyze.
		
	Returns:
		# of misplaced tiles.
	"""
	
	misplaced = 0;
	
	for i in range(0, 3):
		for j in range(0, 3):
			if(b.board[i][j] != 3*i + j):
				misplaced = misplaced + 1
	
	return misplaced

def h2(b):
	"""
	Heuristic function: returns sum of distances from goal positions.
	
	Parameters:
		Board to analyze.
		
	Returns:
		# of misplaced tiles.
	"""
	
	distance = 0;
	
	for i in range(0, 3):
		for j in range(0, 3):
			distance = distance + abs(i - b.board[i][j] / 3)
			distance = distance + abs(j - b.board[i][j] % 3)
	
	return distance

