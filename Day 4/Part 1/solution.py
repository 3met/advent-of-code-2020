
"""
Advent of Code 2020
By Emet Behredt
Day 4
Section 1
"""

import os
import re

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split('\n\n')


def main(puzzle_input):
	# Main Function
	expressions = [
		'byr',
		'iyr',
		'eyr',
		'hgt',
		'hcl',
		'ecl',
		'pid',
	]

	count = 0

	for passport in puzzle_input:
		for e in expressions:
			if not re.search(e, passport):
				break
		else:
			count += 1

	print(count)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
