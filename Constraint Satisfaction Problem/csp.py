from sys import argv

count = 0

# Checking the validity for a value to present at any particular location
def check_valid(sudoku, x, y, value):

	for i in range(9):

		# Checking the row or column if the is already present or not
		if (sudoku[x][i] == value and i != y) or (sudoku[i][y] == value and i != x):
			return False

	# Checking the validity inside the box for the value
	corner_x = (x // 3) * 3
	corner_y = (y // 3) * 3

	for i in range(3):
		for j in range(3):

			if sudoku[corner_x + i][corner_y + j] == value:
				return False

	return True

# Definition of the function for solving sudoku
def solve(sudoku, current, to_be_filled, valid_values):

	global count

	# Increasing the count of steps by one
	count += 1

	# Checking if all the variables are filled
	if len(to_be_filled) == current:
		return True

	# Getting the node number which should be filled
	node = to_be_filled[current][1]

	# Assigning the the values from the valid list
	for i in valid_values[node]:

		# Checking if the assigned value is valid or not
		if not check_valid(sudoku, node // 9, node % 9, i):

			# Skipping the rest part if not valid
			continue

		# Assigning the value to the sudoku
		sudoku[node // 9][node % 9] = i

  		# Solving for other variables
		done = solve(sudoku, current + 1, to_be_filled, valid_values)

		# If the chosen value for the variable is correct
		if done:

			# Returning the solved sudoku
			return True

		# Removing the assigned value if not correct
		sudoku[node // 9][node % 9] = 0

	# Returning false if all the values are False to choose the value of previous variable correctly
	return False

def make_sudoku():

	# Opening the file containing sudoku
	sudoku_file = open(argv[1], "r")

	sudoku = []

	# Getting all the lines in the file
	lines = sudoku_file.readlines()

	for line in lines:

		temp = []

		for i in line.split():

			temp.append(0 if i[0] in ['x', 'X'] else int(i))

		sudoku.append(temp)

	return sudoku

def make_values(sudoku):

	valid_values = []

	for i in range(9):
		for j in range(9):

			temp = []

			if sudoku[i][j]:

				temp.append(-1)
				valid_values.append(temp)
				continue

			temp += [values for values in range(1, 10) if check_valid(sudoku, i, j, values)]
			valid_values.append(temp)

	return valid_values

def print_solution(sudoku):

	# Printing the solution
	print("The solution is ")

	for rows in sudoku:
		print(*rows)

## Main function start from here
def main():

	sudoku = make_sudoku()

	# Finding the list of values from the domain which may satisfy the constraint for all the variables
	valid_values = make_values(sudoku)

	# Finding the order in which the variables will be filled this is based on the number of valid values for each variable
	# The variable which has the lower number of valid values will be filled first
	to_be_filled = sorted([[len(valid_values[i]), i] for i in range(81) if valid_values[i] != [-1]])

	# Running the solving function for the sudoku
	solve(sudoku, 0, to_be_filled, valid_values)

	# Printing the solution
	print_solution(sudoku)

	# Printing the count value
	print("The number of steps taken is:", count)

if __name__ == "__main__":
	main()
