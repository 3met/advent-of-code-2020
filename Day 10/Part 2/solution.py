
"""
Advent of Code 2020
By Emet Behrendt
Day 10
Section 2
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split()


class Adapter:
	'''
		Contains data about the adaptor
	'''

	def __init__(self, joltage, n_paths=None):
		self.joltage = joltage
		# Number of paths (NoneType for unknown)
		self.n_paths = n_paths


def main(puzzle_input):
	# Main Function
	adapters = [Adapter(int(x)) for x in puzzle_input]

	# Calculating n paths to outlet
	adapters.append(Adapter(0, n_paths=1))	# outlet
	adapters.sort(key=lambda a: a.joltage)
	adapters.append(Adapter(adapters[-1].joltage + 3))	# device

	max_dif = 3	# Max difference

	for i in range(1, len(adapters)):
		adapters[i].n_paths = 0

		# Find the sum of n_paths between all the possible connections
		for j in range(1, max_dif+1):	# Limits the distance to 3 apart
			dif = abs(adapters[i].joltage - adapters[i-j].joltage)
			if dif > max_dif:
				break
			else:
				adapters[i].n_paths += adapters[i-j].n_paths

	# Total number of paths from phone to outlet
	print(adapters[-1].n_paths)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
