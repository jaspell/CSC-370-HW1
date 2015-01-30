#!/usr/bin/env python

"""Client code for HW 1 (8-puzzle A* search)."""

import random
from collections import deque

import board
import astar_search

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def main():
	
	random.seed()
	
	table1 = []
	table2 = []
	table3 = []
	
	m = 100
	
	for i in range(0, 12):
		
		table1.append(deque(maxlen = m))
		table2.append(deque(maxlen = m))
		table3.append(deque(maxlen = m))

	while table_open(table1, m):

		b = board.Board()

		scramble(b)

		#print b
		
		search2 = astar_search.a_star(b, 2)

		#print "Result: " + str(search2)

		d = search2[1]
		i = d / 2 - 1
	
		if d % 2 == 0 and d > 0 and d < 25 and len(table1[i]) < m:
			
			search1 = astar_search.a_star(b, 1)
			search3 = astar_search.a_star(b, 3)

			#print "Depth " + str(d) + ": " + str(len(table1[i]) + 1) + " / " + str(m)

			print "Result 1: " + str(search1) 
			print "Result 2: " + str(search2)
			print "Result 3: " + str(search3)
			
			table1[i].append(search1)
			table2[i].append(search2)
			table3[i].append(search3)
	
	#insert code for printing table results
	
	# Results will store cost and ebf as a tuple at same index as tables.
	results1 = []
	results2 = []
	results3 = []
	
	for deq in table1:

		cost = 0
		ebf = 0

		for run in deq:
			cost += run[0]
			ebf += run[2]

		cost = cost / float(m)
		ebf = ebf / float(m)

		results1.append((round(cost), ebf))

	for deq in table2:

		cost = 0
		ebf = 0

		for run in deq:
			cost += run[0]
			ebf += run[2]

		cost = cost / float(m)
		ebf = ebf / float(m)

		results2.append((round(cost), ebf))
	
	#"""
	for deq in table3:

		cost = 0
		ebf = 0

		for run in deq:
			cost += run[0]
			ebf += run[2]

		cost = cost / float(m)
		ebf = ebf / float(m)

		results3.append((round(cost), ebf))
	#"""

	for i in range(len(results1)):
		print str(2*(i+1)) + "  " + str(results1[0]) + "  " + str(results1[1])

	for i in range(len(results2)):
		print str(2*(i+1)) + "  " + str(results2[0]) + "  " + str(results2[1])
	
	for i in range(len(results3)):
		print str(2*(i+1)) + "  " + str(results3[0]) + "  " + str(results3[1])
	
def table_open(table, m):
	
	for deq in table:
		
		if len(deq) < m:
			
			return True
		
	return False
	
def scramble(b):

	moves = random.randint(2, 100)

	#print moves
	
	for i in range(0, moves):
		
		r = random.randint(1, 4)
		
		if r == 1: b.swap_up()
		elif r == 2: b.swap_down()
		elif r == 3: b.swap_left()
		else: b.swap_right()

if __name__ == "__main__":
	main()