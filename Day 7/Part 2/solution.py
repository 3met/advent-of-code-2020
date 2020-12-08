
"""
Advent of Code 2020
By Emet Behrendt
Day 7
Section 2
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split('\n')


class Bag:
	bag_index = {}

	def __init__(self, name, children):
		Bag.bag_index[name] = self
		self.children = dict(children)

		# Number of children (including grandchildren, etc) 
		# that the bag contains
		if len(children) == 0:
			self.n_children = 0
		else:
			self.n_children = None

	def calc_n_children(self):
		if self.n_children is not None:
			return self.n_children
		else:
			total = 0
			for c in self.children:				
				# Number of specific child bag
				total += self.children[c]
				# Number of bag A * number of sub-bag that bag A has
				total += self.children[c] * Bag.bag_index[c].calc_n_children()
				self.n_children = total
			return total


def main(puzzle_input):
	# Main Function

	# --- Parse Input ---
	for line in puzzle_input:
		words = line.split(' ')
		# Note that names are always two words in length
		name = ' '.join(words[0:2])
		children = {}

		if words[4] != 'no':	# Account for when there are no bags
			# Pair child with number of that child
			children[' '.join(words[5:7])] = int(words[4])

			# Loop through remaining children bags
			# Note that distancing between bag names is constant
			i = 0
			while True:
				i += 1
				if bool(words[5+i*4:7+i*4]):
					children[' '.join(words[5:7])] = int(words[4])
					children[' '.join(words[5+i*4:7+i*4])] = int(words[4+i*4])
				else:
					break

		Bag(name, children)

	# --- Calculate Valid Bags ---
	total = Bag.bag_index['shiny gold'].calc_n_children()

	print(total)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
