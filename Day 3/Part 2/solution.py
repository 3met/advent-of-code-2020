
"""
Advent of Code 2020
By Emet Behredt
Day 3
Section 2
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split()


def count_trees(dx, dy, tree_map):
	x = 0
	y = 0

	width = len(tree_map[0])
	height = len(tree_map)

	count = 0

	for _ in range(0, height, dy):
		if tree_map[y][x] == '#':
			count += 1

		x += dx
		x %= width
		y += dy

	return count

def main(puzzle_input):
	# Main Function
	total = 1

	total *= count_trees(1, 1, puzzle_input)
	total *= count_trees(3, 1, puzzle_input)
	total *= count_trees(5, 1, puzzle_input)
	total *= count_trees(7, 1, puzzle_input)
	total *= count_trees(1, 2, puzzle_input)

	print(total)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
