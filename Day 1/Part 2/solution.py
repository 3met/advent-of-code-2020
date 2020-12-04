
"""
Advent of Code 2020
By Emet Behredt
Day 1
Section 2
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split()


def main(puzzle_input):
	input_set = set(puzzle_input)

	for i in range(len(puzzle_input)-1):
		num_1 = int(puzzle_input[i])
		for j in range(i+1, len(puzzle_input)):
			num_2 = int(puzzle_input[j])
			if str(2020-(num_1+num_2)) in input_set:
				return num_1 * num_2 * (2020-(num_1+num_2))


if __name__ == '__main__':
	print(main(PUZZLE_INPUT))
