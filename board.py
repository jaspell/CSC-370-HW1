"""8-puzzle board object for HW 1 (8-puzzle A* search)."""

from copy import deepcopy

__author__ = "Jackson Spell"
__email__ = "jaspell@davidson.edu"

class Board:
	"""
	An 8-puzzle board.
	"""

	goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

	def __init__(self):

		self.board = Board.goal_state
		self.i = 0
		self.j = 0

	def up(self):
		"""
		Returns new Board state; empty square and square above are swapped.

		Parameters:
			none

		Returns:
			altered Board
		"""

		if self.i != 0:

			temp_board = deepcopy(self.board)

			temp_board[temp_board.i][temp_board.j] = temp_board[temp_board.i-1][temp_board.j]
			temp_board[temp_board.i-1][temp_board.j] = 0
			temp_board.i = temp_board.i - 1

			return temp_board

	def down(self):
		"""
		Returns new Board state; empty square and square below are swapped.

		Parameters:
			none

		Returns:
			altered Board
		"""

		if self.i != 2:

			temp_board = deepcopy(self.board)

			temp_board[temp_board.i][temp_board.j] = temp_board[temp_board.i+1][temp_board.j]
			temp_board[temp_board.i+1][temp_board.j] = 0
			temp_board.i = temp_board.i + 1

			return temp_board

	def left(self):
		"""
		Returns new Board state; empty square and square to left are swapped.

		Parameters:
			none

		Returns:
			altered Board
		"""

		if self.j != 0:

			temp_board = deepcopy(self.board)

			temp_board[temp_board.i][temp_board.j] = temp_board[temp_board.i][temp_board.j-1]
			temp_board[temp_board.i][temp_board.j-1] = 0
			temp_board.j = temp_board.j - 1

			return temp_board

	def right(self):
		"""
		Returns new Board state; empty square and square to right are swapped.

		Parameters:
			none

		Returns:
			altered Board
		"""

		if self.j != 2:

			temp_board = deepcopy(self.board)

			temp_board[temp_board.i][temp_board.j] = temp_board[temp_board.i][temp_board.j+1]
			temp_board[temp_board.i][temp_board.j+1] = 0
			temp_board.j = temp_board.j + 1

			return temp_board

	def moves(self):
		"""
		Return the possible moves given the board's current state.

		Parameters:
			none

		Returns:
			list - boards representing possible moves from the current position
		"""

		output = []

		if self.i != 0:
			output.append(self.up())

		if self.i != 2:
			output.append(self.down())

		if self.j != 0:
			output.append(self.left())

		if self.j != 2:
			output.append(self.right())
			
		return output

	def __str__(self):
		"""
		Return a readable representation of a puzzle board.

		Parameters:
			none

		Returns:
			string - human-readable representation of the board
		"""

		output = "+"

		for col in self.board[0]:
			output += "-"

		output += "+\n"

		for row in self.board:
			output += "|" 
			for square in row:
				if square == 0:
					output += " "
				else:
					output += str(square)
			output += "|\n"

		output += "+"

		for col in self.board[0]:
			output += "-"

		output += "+"	

		return output	
