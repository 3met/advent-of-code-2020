
"""
Advent of Code 2020
By Emet Behrendt
Day 7
Section 1
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
		self.children = set(children)

		# Denote whether the bag can contain a shiny gold bag
		# directly or through is children; 'None' indicates the 
		# value is not known
		if 'shiny gold' in children:
			self.has_gold = True
		else:
			self.has_gold = None

	def set_child(self, child):
		children.add(child)

	def check_gold(self):
		if self.has_gold:
			return True
		elif self.has_gold == False:
			return False
		else:
			for bag in self.children:
				if Bag.bag_index[bag].check_gold():
					#self.has_gold = True
					return True
			#self.has_gold = False
			return False


def main(puzzle_input):
	# Main Function

	# --- Parse Input ---
	for line in puzzle_input:
		words = line.split(' ')
		# Note that names are always two words in length
		name = ' '.join(words[0:2])
		children = []

		if words[4] != 'no':	# Account for when there are no bags
			children.append(' '.join(words[5:7]))

			# Loop through remaining children bags
			# Note that distancing between bag names is constant
			i = 0
			while True:
				i += 4
				if bool(words[5+i:7+i]):
					children.append(' '.join(words[5+i:7+i]))
				else:
					break

		Bag(name, children)

	# --- Calculate Valid Bags ---
	total = 0

	for bag in Bag.bag_index.values():
		if bag.check_gold():
			total += 1

	print(total)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
