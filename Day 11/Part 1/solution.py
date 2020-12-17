
"""
Advent of Code 2020
By Emet Behrendt
Day 11
Section 1
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split('\n')


class Node:
	def __init__(self, occupied, adjacent=[], next_occupied=None):
		self.occupied = occupied
		self.adjacent = list(adjacent)
		self.next_occupied = next_occupied

	def add_adjacent(self, node):
		self.adjacent.append(node)

	def calc_next(self):
		n_occ_adj = self._n_occ_adj()
		# If a seat is empty (L) and there are no occupied seats
		# adjacent to it, the seat becomes occupied.
		if n_occ_adj == 0:
			self.next_occupied = True
		# If a seat is occupied (#) and four or more seats adjacent
		# to it are also occupied, the seat becomes empty.
		elif n_occ_adj >= 4:
			self.next_occupied = False
		# Otherwise, the seat's state does not change.
		else:
			self.next_occupied = self.occupied

	def update(self):
		if self.occupied != self.next_occupied:
			self.occupied = self.next_occupied
			return True
		return False

	def _n_occ_adj(self):
		"""
		Number of occupied adjacent seat
		"""
		n = 0
		for adj in self.adjacent:
			if adj.occupied:
				n += 1
		return n


def main(puzzle_input):
	# Main Function
	node_grid = []
	node_set = set()

	for row in puzzle_input:
		node_grid.append([])
		for cell in row:
			if cell == 'L':
				node = Node(True)
				node_grid[-1].append(node)
				node_set.add(node)
			else:
				node_grid[-1].append(None)

	for i in range(len(node_grid)):
		for j in range(len(node_grid[i])):
			if node_grid[i][j] is not None:
				for k in range(-1, 2):
					for l in range(-1, 2):
						if (k != 0 or l != 0):	# Ensure difference coords
							di = i + k	# pos for connection
							dj = j + l
							
							if di >= 0 and dj >= 0 and di < len(node_grid) and dj < len(node_grid[i]):
								if node_grid[di][dj] is None:
									continue

								node_grid[i][j].add_adjacent(node_grid[di][dj])

	del node_grid

	while True:
		for node in node_set:
			node.calc_next()

		changed = False
		for node in node_set:
			changed = node.update() or changed 

		if not changed:
			break

	counter = 0
	for node in node_set:
		if node.occupied:
			counter += 1

	print(counter)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
