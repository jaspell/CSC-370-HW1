#!/usr/bin/env python

"""Client code for HW 1 (8-puzzle A* search)."""

import board
import astar_search
import random
from collections import deque

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def main():
    
    random.seed()
    
	b = board.Board()
    
    table1 = []
    table2 = []
    #table3 = []
    
    for i in range(0, 12):
        
        """
        max out deque lengths at 2^d, since there will be no more than
        this many boards with optimal solutions of a given depth.
        """
        d = 2 * i + 2
        m = 100
        if 2 ** d < 100: m = 2 ** d
        table1.append(deque(maxlen = m))
        table2.append(deque(maxlen = m))
        #table3.append(deque(maxlen = m))
    
    while table_open(table1):
        
        scramble(b)
        
        search1 = astar_search.a_star(b, 1)
        d = search[1]
        i = d / 2 - 1
    
        if d % 2 == 0 and d > 0 and d < 25 and len(table1[i]) < 100:
            
            search2 = astar_search.a_star(b, 2)
            #search3 = astar_search.a_star(b, 3)
            
            table1[i].append(search1)
            table2[i].append(search2)
            #table3[i].append(search3)
    
    #insert code for printing table results
    
    
	print goal
	print astar_search.a_star(goal, 1)
	print astar_search.a_star(goal, 2)
	
	goal.swap_right()
	print goal
	print astar_search.a_star(goal, 1)
	print astar_search.a_star(goal, 2)

	goal.swap_down()
	print goal
	print astar_search.a_star(goal, 1)
	print astar_search.a_star(goal, 2)
    
def table_open(table):
    
    for i in range(0, 12):
        
        if len(table[i]) < 2 ** (2 * i + 2):
            
            return True
        
    return False
    
def scramble(b):
    
    for i in range(0, 50):
        
        r = random.randint(1, 4)
        
        if r == 1: b.swap_up()
        elif r == 2: b.swap_down()
        elif r == 3: b.swap_left()
        else b.swap_right()

if __name__ == "__main__":
	main()