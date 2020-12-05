
"""
Advent of Code 2020
By Emet Behrendt
Day 5
Section 2
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split()

def get_id(bpass):
	row = None
	column = None

	top = 0
	bot = 127

	for letter in bpass[0:7]:
		diff = (bot - top + 1)/2

		if letter == 'F':
			bot -= diff
		else:
			top += diff

	row = top	

	top = 0
	bot = 7

	for letter in bpass[7:10]:
		diff = (bot - top + 1)/2
		
		if letter == 'L':
			bot -= diff
		else:
			top += diff

	column = top

	return int(row * 8 + column)


def main(puzzle_input):
	# Main Function
	taken_seats = []

	for bpass in puzzle_input:
		taken_seats.append(get_id(bpass))

	taken_seats.sort()

	for i in range(0, len(taken_seats)-1):
		if taken_seats[i]+1 != taken_seats[i+1]:
			print(taken_seats[i]+1)
			break
	else:
		print('Not Found.')
		

if __name__ == '__main__':
	main(PUZZLE_INPUT)
