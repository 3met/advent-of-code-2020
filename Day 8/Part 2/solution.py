
"""
Advent of Code 2020
By Emet Behrendt
Day 8
Section 2
"""

import os
import copy

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

	def set_complete(self):
		self.complete = True

	def set_incomplete(self):
		self.complete = False


def check_terminate(boot_code):
	# --- Run Boot Code ---
	i = 0	# code index

	while i < len(boot_code):
		instruction = boot_code[i]

		if instruction.complete:
			return False
		elif instruction.operation == 'jmp':
			i += instruction.value
		else:
			i += 1

		instruction.set_complete()

	return True


def get_accumulator(boot_code):
	# Assumes the boot code does not loop

	accumulator = 0
	i = 0	# code index

	while i < len(boot_code):
		instruction = boot_code[i]

		if instruction.operation == 'acc':
			accumulator += instruction.value
			i += 1
		elif instruction.operation == 'jmp':
			i += instruction.value
		else:
			i += 1

	return accumulator


def main(puzzle_input):
	# Main Function
	# --- Parse Input ---
	boot_code = []

	for operation in puzzle_input:
		operation = operation.split()
		boot_code.append(Instruction(operation[0], int(operation[1])))

	# --- Fix Boot Code ---
	for line in boot_code:
		# -- Modify of Bootcode --
		original = ''

		if line.operation == 'nop':
			original = 'nop'
			line.operation = 'jmp'
		elif line.operation == 'jmp':
			original = 'jmp'
			line.operation = 'nop'
		else:
			continue

		# -- Check if Code will terminate --
		if check_terminate(boot_code):
			accumulator = get_accumulator(boot_code)
			print(accumulator)
			break
		
		# -- Return Boot Code to Original State --
		for modified_line in boot_code:
			modified_line.set_incomplete()

		line.operation = original


if __name__ == '__main__':
	main(PUZZLE_INPUT)
