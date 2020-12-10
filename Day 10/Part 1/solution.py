
"""
Advent of Code 2020
By Emet Behrendt
Day 10
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
	adapters = [int(x) for x in puzzle_input]

	adapters.append(0)	# outlet
	adapters.append(max(adapters) + 3)	# device

	adapters.sort()

	n_one = 0
	n_three = 0

	for i in range(len(adapters) - 1):
		dif = adapters[i+1] - adapters[i]

		if dif == 1:
			n_one += 1
		elif dif == 3:
			n_three += 1

	print(n_one * n_three)

if __name__ == '__main__':
	main(PUZZLE_INPUT)
