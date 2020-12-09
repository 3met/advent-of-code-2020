
"""
Advent of Code 2020
By Emet Behredt
Day 9
Section 2
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
	# Main Function
	cypher = [int(x) for x in puzzle_input]

	invalid_n = 0

	# Main Function
	for i in range(0, len(cypher)-26):
		if not valid_xmas(cypher[i:i+25], cypher[i+25]):
			invalid_n = cypher[i+25]
			break

	bot = 0
	top = 1

	while True:
		if sum(cypher[bot:top+1]) == invalid_n:
			print(min(cypher[bot:top+1]) + max(cypher[bot:top+1]))
			break
		elif sum(cypher[bot:top+1]) >= invalid_n:
			bot += 1
		else:
			top += 1


if __name__ == '__main__':
	main(PUZZLE_INPUT)
