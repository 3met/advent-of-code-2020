
"""
Advent of Code 2020
By Emet Behredt
Day 2
Section 2
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.readlines()


def main(puzzle_input):
	# Main Function
	n_valid = 0

	for line in puzzle_input:
		buff = line.split(': ')
		rules = buff[0]
		password = buff[1]

		buff = rules.split(' ')
		ab = buff[0]
		letter = str(buff[1])

		buff = ab.split('-')
		a = int(buff[0])-1
		b = int(buff[1])-1

		if (password[a] == letter and password[b] != letter) or (password[a] != letter and password[b] == letter):
			n_valid += 1

	print(n_valid)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
