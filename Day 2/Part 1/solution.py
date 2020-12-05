
"""
Advent of Code 2020
By Emet Behrendt
Day 2
Section 1
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.readlines()


def main(puzzle_input):
	n_valid = 0

	for line in puzzle_input:
		buff = line.split(':')
		rules = buff[0]
		password = buff[1]

		buff = rules.split(' ')
		minmax = buff[0]
		letter = buff[1]

		buff = minmax.split('-')
		minimum = int(buff[0])
		maximum = int(buff[1])

		count = 0
		for x in password:
			if x == letter:
				count += 1 

		if count >= minimum and count <= maximum:
			n_valid += 1

	print(n_valid)

if __name__ == '__main__':
	main(PUZZLE_INPUT)
