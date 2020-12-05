
"""
Advent of Code 2020
By Emet Behrendt
Day 1
Section 1
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split()


def main(puzzle_input):
	puzzle_input = set(puzzle_input)
	for num in puzzle_input:
		if str(2020-int(num)) in puzzle_input:
			return int(num) * (2020-int(num))


if __name__ == '__main__':
	print(main(PUZZLE_INPUT))
