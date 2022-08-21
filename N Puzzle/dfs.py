# Importing the dependencies
from time import time

# CONSTANTS
SOLUTION_PATH_THRESHOLD = 10 ** 10

# This dictionary to store parent of child states and marks the visited states
parent = {}

# This utility function prints the state
def printstate(state):
    print("State: ");
    n = len(state)
    N = int(n ** 0.5)
    for i in range(N):
        print(' '.join(map(str, state[i * N:(i + 1) * N])))
    print('*'*20)
    return ""

# Gets the possible moves from the state
def get_moves(state):

    n = len(state)
    N = int(n ** 0.5)

    # Getting the (x, y) coordinates of the blank space
    row = state.index(0) // N;
    col = state.index(0) % N;

    # Creating a list of possible moves
    moves = []

    # Checking if the blank space can move (up, down, left, right)
    for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:

        # If the move is valid
        if 0 <= i < N and 0 <= j < N:

            # swap the position of the blank space with the position of the tile
            zero_index = state.index(0)
            temp = state[i * N + j]
            state[i * N + j] = state[zero_index]
            state[zero_index] = temp

            # Append the new state to the list of moves
            moves.append(state.copy())

            # swap the position of the blank space with the position of the tile
            # back to its original position
            temp = state[i * N + j]
            state[i * N + j] = state[zero_index]
            state[zero_index] = temp

    return moves

# This function is used to print the solution path.
def print_solution_len(solution):

    solution_path = []

    # Tracing the goal state to the start state path
    while str(solution) in parent:
        solution_path.append(solution)
        solution = parent[str(solution)]

    print(f"Length of solution_path (DFS): {len(solution_path)}\n")

    # If the solution path is less than the threshold
    # Print the solution path
    print('Trying to print solution path...\n')

    if len(solution_path) < SOLUTION_PATH_THRESHOLD:

        print("Solution Path (DFS):")

        for i in reversed(solution_path):
            printstate(i)
            print("\n")
    else:
        print(f'Solution len exceeds {SOLUTION_PATH_THRESHOLD}, abort printing states to avoid performance issues')

# iterative DFS code to reach to goal node
def iterative_dfs(start, goal):

    # Initializing the stack (frontier) with the start node
    frontier = [start]

    # Initializing the visited set (explored) with the start node
    explored = set()
    explored.add(str(start))

    # Initializing the parent dictionary
    parent[str(start)] = None

    # while stack (frontier) is not empty
    while frontier:

        # pop the first element from the stack (frontier)
        node = frontier.pop()

        # if the popped node is the goal node
        if node == goal:
            return goal

        # get the possible moves from the popped node
        for child in get_moves(node):

            # if the child node is not in the explored set
            if str(child) not in explored:

                # add the child node to the stack (frontier) and explored set
                frontier.append(child)
                explored.add(str(child))

                # set the parent of child node to the popped node
                parent[str(child)] = node

# main
if __name__ == '__main__':

    # THE START STATE

    # eg start
    # user types: 7 2 4 5 0 6 8 3 1, then start becomes
    # start = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    start = list(map(int, input("Enter the start state matrix \n").split()))

    # THE GOAL STATE
    # eg goal
    # user types: 0 1 2 3 4 5 6 7 8
    # goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    goal = list(map(int, input("Enter the goal state matrix \n").split()))

    # start the timer
    st = time()

    # call the iterative DFS function
    goal = iterative_dfs(start, goal)

    # stop the timer
    et = time()

    # PRINTING RESULT
    print("Execution Time for DFS:", et - st, "seconds")
    print()
    print_solution_len(goal)

