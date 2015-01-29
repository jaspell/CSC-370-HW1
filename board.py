"""8-puzzle board object for HW 1 (8-puzzle A* search)."""

from copy import deepcopy

__author__ = "Jackson Spell and Ben Wiley"
__email__ = "jaspell@davidson.edu, bewiley@davidson.edu"

class Board:
	"""
	An 8-puzzle board.
	"""

	goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

	def __init__(self, original=None):
		"""
		Board Constructor.

		Parameters:
			original - Board - board to copy

		Returns:
			instantiated copy of the original board
		"""

		if original is None:
			self.board = deepcopy(Board.goal_state)
			self.i = 0
			self.j = 0

		else:
			self.board = deepcopy(original.board)
			self.i = original.i
			self.j = original.j

	def swap_up(self):
		"""
		Swaps the empty square and the square above.
		
		Parameters:
			none
		
		Returns:
			nothing
		"""
		
		if self.i != 0:
			
			self.board[self.i][self.j] = self.board[self.i-1][self.j]
			self.board[self.i-1][self.j] = 0
			self.i = self.i - 1

	def swap_down(self):
		"""
		Swaps the empty square and the square below.
		
		Parameters:
			none
		
		Returns:
			nothing
		"""

		if self.i != 2:
		
			self.board[self.i][self.j] = self.board[self.i+1][self.j]
			self.board[self.i+1][self.j] = 0
			self.i = self.i + 1

	def swap_left(self):
		"""
		Swaps the empty square and the square to the left.
		
		Parameters:
			none
		
		Returns:
			nothing
		"""

		if self.j != 0:
		
			self.board[self.i][self.j] = self.board[self.i][self.j-1]
			self.board[self.i][self.j-1] = 0
			self.j = self.j - 1

	def swap_right(self):
		"""
		Swaps the empty square and the square to the right.
		
		Parameters:
			none
		
		Returns:
			nothing
		"""

		if self.j != 2:
		
			self.board[self.i][self.j] = self.board[self.i][self.j+1]
			self.board[self.i][self.j+1] = 0
			self.j = self.j + 1

	def up(self):
		"""
		Returns new Board state; empty square and square above are swapped.

		Parameters:
			none

		Returns:
			altered Board
		"""

		if self.i != 0:

			temp_board = Board(self)
			temp_board.swap_up()

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

			temp_board = Board(self)
			temp_board.swap_down()

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

			temp_board = Board(self)
			temp_board.swap_left()
			
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

			temp_board = Board(self)
			temp_board.swap_right()
			
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

	def __cmp__(self, other):
		"""
		Compare self to other.

		Parameters:
			other - Board - board to compare to

		Returns:
			int - 0 if boards are identical, nonzero otherwise
		"""

		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if self.board[i][j] != other.board[i][j]:
					return 1

		return 0
