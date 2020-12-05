
"""
Advent of Code 2020
By Emet Behrendt
Day 5
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
	highest = 0
	row = None
	column = None

	for seat in puzzle_input:

		top = 0
		bot = 127

		for letter in seat[0:7]:
			diff = (bot - top + 1)/2

			if letter == 'F':
				bot -= diff
			else:
				top += diff

		row = top	

		top = 0
		bot = 7

		for letter in seat[7:10]:
			diff = (bot - top + 1)/2
			
			if letter == 'L':
				bot -= diff
			else:
				top += diff

		column = top

		iden = row * 8 + column
		highest = max(highest, iden)

	print(highest)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
