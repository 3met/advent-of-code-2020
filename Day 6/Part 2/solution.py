
"""
Advent of Code 2020
By Emet Behrendt
Day 6
Section 2
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
		group = group.split('\n')	# Remove '\n' seperating people
		group_answers = []

		for person in group:
			person_answers = set()

			for letter in person:
				if letter not in person_answers:
					person_answers.add(letter)

			group_answers.append(person_answers)

		universal = group_answers[0]
		for answer in group_answers[1:]:
			universal = universal.intersection(answer)

		total += len(universal)

	print(total)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
