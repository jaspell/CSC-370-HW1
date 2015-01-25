#!/usr/bin/env python

"""Client code for HW 1 (8-puzzle A* search)."""

import board
import astar_search

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def main():

	goal = board.Board()
	print goal
	
	goal.swap_right()
	print goal

	goal.swap_down()
	print goal

	for b in goal.moves():
		print b

if __name__ == "__main__":
	main()