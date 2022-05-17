### PARAMETERS (can be changed):

SOLUTION_PATH_THRESHOLD: This is the threshold length upto which the program can print the path, 
but if the path length increases this threshold we do not print the path to avoid performance issues.

### INPUT:

#### [START STATE] 

2 space separated integers denoting the start cell of the grid given in the question (0-indexed).

Input according to the start state given in the question should be: 5 3

#### [GOAL STATE] 

2 space separated integers denoting the goal cell of the grid given in the question (0-indexed).

Input according to the goal state given in the question should be: 2 2

### OUTPUT:

Prints the duration of time it took to find the goal state.

Prints the length of the path from start to goal state.

Outputs the path to goal state if the length of the solution path is less than the
threshold length allowed.
