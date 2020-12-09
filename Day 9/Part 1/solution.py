
"""
Advent of Code 2020
By Emet Behrendt
Day 9
Section 1
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split()


def valid_xmas(numbers, target):
	numbers = set(numbers)

	for n in numbers:
		remainder = target - n
		if remainder in numbers and remainder*2 != target:
			return True

	return False


def main(puzzle_input):
	cypher = [int(x) for x in puzzle_input]

	# Main Function
	for i in range(0, len(cypher)-26):
		if not valid_xmas(cypher[i:i+25], cypher[i+25]):
			print(cypher[i+25])
			break


if __name__ == '__main__':
	main(PUZZLE_INPUT)
