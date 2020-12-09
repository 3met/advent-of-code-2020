
"""
Advent of Code 2020
By Emet Behrendt
Day 8
Section 1
"""

import os

SELF_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')

# Fetch puzzle input
with open(INPUT_PATH, 'r') as file:
	PUZZLE_INPUT = file.read().split('\n')


class Instruction:
	def __init__(self, operation, value):
		# operation as string, value as int
		self.operation = operation
		self.value = value
		self.complete = False

	def mark_complete(self):
		self.complete = True


def main(puzzle_input):
	# Main Function
	# --- Parse Input ---
	boot_code = []

	for operation in puzzle_input:
		operation = operation.split()
		boot_code.append(Instruction(operation[0], int(operation[1])))

	# --- Run Boot Code ---
	accumulator = 0
	i = 0	# code index

	while True:
		instruction = boot_code[i]

		if instruction.complete:
			break
		elif instruction.operation == 'acc':
			accumulator += instruction.value
			i += 1
		elif instruction.operation == 'jmp':
			i += instruction.value
		else:
			i += 1

		instruction.mark_complete()

	print(accumulator)


if __name__ == '__main__':
	main(PUZZLE_INPUT)
