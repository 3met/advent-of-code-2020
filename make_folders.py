
import os

SELF_DIR = os.path.dirname(__file__)

def gen_start_code(name, year, day, section):
	# Generate start code for program
	return '\n'.join([
		(''),
		('"""'),
		(f'Advent of Code {str(year)}'),
		(f'By {name}'),
		(f'Day {str(day)}'),
		(f'Section {str(section)}'),
		('"""'),
		(''),
		('import os'),
		(''),
		('SELF_DIR = os.path.dirname(__file__)'),
		("INPUT_PATH = os.path.join(SELF_DIR, 'puzzle_input.txt')"),
		(''),
		('# Fetch puzzle input'),
		("with open(INPUT_PATH, 'r') as file:"),
		('\tPUZZLE_INPUT = file.read().split()'),
		(''),
		(''),
		('def main(puzzle_input):'),
		('\t# Main Function'),
		('\tpass'),
		(''),
		(''),
		("if __name__ == '__main__':"),
		('\tmain(PUZZLE_INPUT)'),
		(''),
	])

def create_folder(name_format=f'%s', target_dir=SELF_DIR):
	"""
	Creates numbered folders
	"""

	for day in range(1, 26): # 25 days until of calendar
		# Create numbered folder in target directory
		dir_name = name_format.replace(f'%s', str(day))
		dir_src = os.path.join(target_dir, dir_name)
		os.mkdir(dir_src)

		# Create directories for part one and two
		dir_1 = os.path.join(dir_src, 'Part 1/')
		dir_2 = os.path.join(dir_src, 'Part 2/')
		os.mkdir(dir_1)
		os.mkdir(dir_2)

		# Add starter code
		with open(os.path.join(dir_1, 'solution.py'), 'w') as file:
			start_code = gen_start_code(
				name='Emet Behredt',
				year=2020,
				day=day,
				section=1)
			file.write(start_code)

		with open(os.path.join(dir_2, 'solution.py'), 'w') as file:
			start_code = gen_start_code(
				name='Emet Behrendt',
				year=2020,
				day=day,
				section=2)
			file.write(start_code)

		# Create input file
		open(os.path.join(dir_1, 'puzzle_input.txt'), 'w')
		open(os.path.join(dir_2, 'puzzle_input.txt'), 'w')

if __name__ == '__main__':
	create_folder(name_format=f'Day %s')
