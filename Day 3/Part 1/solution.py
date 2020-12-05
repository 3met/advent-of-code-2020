
"""
Advent of Code 2020
By Emet Behrendt
Day 3
Section 1
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split()


def main(puzzle_input):
	# Main Function
	x = 0
	y = 0

	dx = 3
	dy = 1

	width = len(puzzle_input[0])
	height = len(puzzle_input)

	count = 0

	for _ in range(0, height, dy):
		if puzzle_input[y][x] == '#':
			count += 1

		x += dx
		x %= width
		y += dy

	print(count)




if __name__ == '__main__':
	main(PUZZLE_INPUT)
