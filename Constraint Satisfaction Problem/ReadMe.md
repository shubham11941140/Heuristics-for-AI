# Constraint Satisfaction Problem - Sudoku Solver

This the Python code for solving a sudoku based on Constraint satisfaction problem algorithm

## Prerequisites

Python version 3.10 it may work on other versions but i have coded in this version

## INPUT

Create a file in same folder as of the code file named "input.txt" and type the sudoku row wise inside it putting 'x' or 'X' in places need to be filled with solution
each value in the row should be separated with a space

for example:-

```
X 1 X 2 5 7 9 3 X
7 3 X 4 9 8 X 1 6
8 5 9 3 0 6 X 4 2
X 6 1 5 X 2 3 7 4
2 7 4 9 3 1 X 8 5
3 8 X 6 7 4 2 9 X
1 2 3 8 6 X 4 5 7
X 9 8 X 4 5 1 2 X
5 4 7 1 2 3 X 6 9
```

## HOW TO RUN THE CODE

The run the code to open the terminal move the directory where the code is present

type the command in windows :- (Let us say that the input file is eg_sudoku.txt)

```
python question1.py eg_sudoku.txt
```

For ```input.txt```:

```
python question1.py input.txt
```

for linux try the same command or try with "python3" instead of "python"


## OUTPUT

the output will be completed sudoku with the number of steps taken printed after the solution

for example :-

The solution is:
```
4 1 6 2 5 7 9 3 8
7 3 2 4 9 8 5 1 6
8 5 9 3 1 6 7 4 2
9 6 1 5 8 2 3 7 4
2 7 4 9 3 1 6 8 5
3 8 5 6 7 4 2 9 1
1 2 3 8 6 9 4 5 7
6 9 8 7 4 5 1 2 3
5 4 7 1 2 3 8 6 9
```
The number of steps taken is 2

### The solution to the given problem is:

![image](https://user-images.githubusercontent.com/63910248/168804517-f2ee9152-f127-45eb-a729-b9c7e3e75678.png)

