
from copy import deepcopy

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
		Move the empty square up.

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
		Move the empty square down.

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
		Move the empty square left.

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
		Move the empty square right.

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