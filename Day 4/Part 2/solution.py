
"""
Advent of Code 2020
By Emet Behrendt
Day 4
Section 2
"""

import os
import re
from datetime import datetime

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split('\n\n')


def main(puzzle_input):
	# Main Function
	expressions = [
		'byr:(19[2-9][0-9]|200[0-2])',
		'iyr:(201[0-9]|2020)',
		'eyr:(202[0-9]|2030)',
		'hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)',
		'hcl:#[0-9a-f]{6}',
		'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
		'pid:[0-9]{9}([^0-9]|$)',
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
