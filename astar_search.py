"""A* search algorithm for HW 1 (8-puzzle A* search)."""

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def a_star(b):
    """
    Runs A* algorithm to find optimal path from current to goal state.
    
    Parameters:
        b - Board - starting board state
    
    Returns:
        2-tuple containing two 3-tuples:
            ((h1 nodes generated, h2 nodes generated, h3 nodes generated),
             (h1 effective branching factor, h2 effective branching factor,
              h3 effective branching factor))
    """
    
    open_set = [b] #priority queue of Boards
    closed_set = [] #
    
    

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