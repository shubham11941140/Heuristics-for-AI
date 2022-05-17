### This set of inputs, outputs and parameters are applicable to all the parts of the problem i.e. for BFS, DFS and A* algorithm.

### PARAMETERS (can be changed):

SOLUTION_PATH_THRESHOLD: This is the threshold length upto which the program can print the path, 
but if the path length increases this threshold we do not print the path to avoid performance issues.

### INPUT:
If you want to input this N-puzzle's start state: (0 represents the blank tile)

    7 | 2 | 4
    --+---+--
    5 | 0 | 6
    --+---+--
    8 | 3 | 1

Then the input should be:

START_STATE: 7 2 4 5 0 6 8 3 1

If you want to input this N-puzzle's goal state:

    0 | 1 | 2
    --+---+---
    3 | 4 | 5
    --+---+---
    6 | 7 | 8

Then the input should be:

GOAL_STATE: 0 1 2 3 4 5 6 7 8

### OUTPUT:

Prints the duration of time it took to find the goal state.

Prints the length of the path from start to goal state.

Outputs the path to goal state if the length of the solution path is less than the
threshold length allowed.
