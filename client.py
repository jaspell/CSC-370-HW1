#!/usr/bin/env python

"""Client code for HW 1 (8-puzzle A* search)."""

import board
import astar_search

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def main():

	goal = board.Board()
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

if __name__ == "__main__":
	main()