"""A* search algorithm for HW 1 (8-puzzle A* search)."""

import Queue

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def a_star(b, fcn):
    """
    Runs A* algorithm to find optimal path from current to goal state.
    
    Parameters:
        b - Board - starting board state
        fcn - integer - which heuristic to use
    
    Returns:
        2-tuple: (cost, effective branching factor)
    """
    
    open_set = Queue.PriorityQueue() # set of tuples: (f(n), g(n), h(n), Board)
    closed_set = [] # set of nodes already expanded
    
    h = None
    if fcn == 1: h = h1(b)
    elif fcn == 2: h = h2(b)
    else: h = h3(b)
    
    open_set.put((h, 0, h, b))
    
    depth = None
    
    done = False
    
    while not done:
        
        node = open_set.get()
        closed_set.put(node)
        
        if node[2] == 0:
            
            # heuristic == 0
            done = True
            depth = node[1]
            
        else:
            
            g = node[1] + 1
            front = n.moves()
            
            for n in front:
                
                if n not in closed_set:
                    
                    if fcn == 1: h = h1(n)
                    elif fcn == 2: h = h2(n)
                    else: h = h3(n)
                    
                    open_set.put((g+h, g, h, n))
    
    cost = len(closed_set) # + len(open_set) [do we need this?]
    ebf = None # we need to figure out how to actually calculate this
    
    return (cost, ebf)
    

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