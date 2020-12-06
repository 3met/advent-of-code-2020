
"""
Advent of Code 2020
By Emet Behrendt
Day 6
Section 1
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split('\n\n')


def main(puzzle_input):
	# Main Function
	total = 0

	for group in puzzle_input:
		group = group.replace('\n', '')	# Remove '\n' seperating people
		yes_answers = set()

		for letter in group:
			if letter not in yes_answers:
				yes_answers.add(letter)

		total += len(yes_answers)

	print(total)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
