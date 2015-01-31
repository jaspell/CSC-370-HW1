#!/usr/bin/env python

"""Client code for HW 1 (8-puzzle A* search)."""

import random
from collections import deque

import numpy
from scipy import stats

import board
import astar_search

__author__ = "Ben Wiley and Jackson Spell"
__email__ = "bewiley@davidson.edu, jaspell@davidson.edu"

def main():

	m = 100
	confidence = 0.95
	
	random.seed()
	
	table1 = []
	table2 = []
	table3 = []
	
	for i in range(0, 12):
		
		table1.append(deque(maxlen = m))
		table2.append(deque(maxlen = m))
		table3.append(deque(maxlen = m))

	while table_open(table1, m):

		b = board.Board()

		scramble(b)

		#print b
		
		search3 = astar_search.a_star(b, 3)

		#print "Result: " + str(search2)

		d = search3[1]
		i = d / 2 - 1
	
		if d % 2 == 0 and d > 0 and d < 25 and len(table1[i]) < m:
			
			search1 = astar_search.a_star(b, 1)
			search2 = astar_search.a_star(b, 2)

			print "Depth " + str(d) + ": " + str(len(table1[i]) + 1) + " / " + str(m)

			# print "Result 1: " + str(search1) 
			# print "Result 2: " + str(search2)
			# print "Result 3: " + str(search3)
			
			table1[i].append(search1)
			table2[i].append(search2)
			table3[i].append(search3)
	
	#insert code for printing table results
	
	results1 = []
	results2 = []
	results3 = []

	# Populate results tables at indexes matching tables, in the form 
	# ((cost mean, cost 95%), (ebf, ebf 95%)).
	for deq in table1:
		n, min_max, cost_mean, cost_var, skew, kurt = stats.describe([run[0] for run in deq])
		cost_std = numpy.sqrt(cost_var)

		n, min_max, ebf_mean, ebf_var, skew, kurt = stats.describe([run[2] for run in deq])
		ebf_std = numpy.sqrt(ebf_var)

		cost_conf = 1.96*cost_std/numpy.sqrt(m)
		ebf_conf = 1.96*ebf_std/numpy.sqrt(m)

		results1.append(((round(cost_mean), round(cost_conf, 2)), 
						 (round(ebf_mean, 2), round(ebf_conf, 2))))
	
	for deq in table2:
		n, min_max, cost_mean, cost_var, skew, kurt = stats.describe([run[0] for run in deq])
		cost_std = numpy.sqrt(cost_var)

		n, min_max, ebf_mean, ebf_var, skew, kurt = stats.describe([run[2] for run in deq])
		ebf_std = numpy.sqrt(ebf_var)

		cost_conf = 1.96*cost_std/numpy.sqrt(m)
		ebf_conf = 1.96*ebf_std/numpy.sqrt(m)

		results2.append(((round(cost_mean), round(cost_conf, 2)), 
						 (round(ebf_mean, 2), round(ebf_conf, 2))))

	for deq in table3:
	 	n, min_max, cost_mean, cost_var, skew, kurt = stats.describe([run[0] for run in deq])
	 	cost_std = numpy.sqrt(cost_var)

	 	n, min_max, ebf_mean, ebf_var, skew, kurt = stats.describe([run[2] for run in deq])
	 	ebf_std = numpy.sqrt(ebf_var)

		cost_conf = 1.96*cost_std/numpy.sqrt(m)
		ebf_conf = 1.96*ebf_std/numpy.sqrt(m)

		results3.append(((round(cost_mean, 2), round(cost_conf, 2)), 
	 					 (round(ebf_mean, 2), round(ebf_conf, 2))))

	for i in range(len(results1)):
		print str(2*(i+1)) + "  " + str(results1[i][0]) + "  " + str(results1[i][1])

	for i in range(len(results2)):
		print str(2*(i+1)) + "  " + str(results2[i][0]) + "  " + str(results2[i][1])
		
	for i in range(len(results3)):
	 	print str(2*(i+1)) + "  " + str(results3[i][0]) + "  " + str(results3[i][1])
	
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