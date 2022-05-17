# Importing Dependencies
from heapq import heappush, heappop
from time import time

# CONSTANTS
SOLUTION_PATH_THRESHOLD = 300

# This dictionary to store parent of child states and marks the visited states
visited = dict()

# This utility function prints the state
def printstate(state):
    n = len(state)
    N = int(n ** 0.5)
    for i in range(N):
        print(' '.join(map(str, state[i * N:(i + 1) * N])))
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

# This function calculates heuristic cost for each tile in a state
# Manhattan Distance Heuristic is used
def heuristic(state, goal, i):

    n = len(state)
    N = int(n ** 0.5)

    row = state.index(i) // N
    col = state.index(i) % N

    final_row = goal.index(i) // N
    final_col = goal.index(i) % N

    return abs(row - final_row) + abs(col - final_col)

# This function calculates the total heuristic cost of the state
def full(state, goal, n):
    return sum([heuristic(state, goal, i) for i in range(n)])

# This function implements the A* search algorithm
def a_star(start, goal, n):

    # Create a priority queue
    pq = []

    # Push the initial state to the priority queue
    heappush(pq, (full(start, goal, n), start))

    # Create a list to store the visited states and mark the start state as visited
    # by marking the parent of start as None
    visited[str(start)] = None

    # While the priority queue is not empty
    while pq:

        # Pop the state from the priority queue
        state = heappop(pq)[1]

         # If the state is the goal state
        if state == goal:

            # Return the solution path
            return visited

        # Get the possible moves from the state
        moves = get_moves(state)

        # For each move
        for move in moves:

            # Push the move to the priority queue if not visited
            if str(move) not in visited.keys():

                # Mark the move as visited by setting the parent of the move as the current state
                visited[str(move)] = state
                heappush(pq, (full(move, goal, n), move))

# This function is used to print the solution path.
def print_solution_len(solution):

    solution_path = []

    # Tracing the goal state to the start state path
    while str(solution) in visited.keys():
        solution_path.append(solution)
        solution = visited[str(solution)]

    print(f"Length of solution_path (A*): {len(solution_path)}\n")

    # If the solution path is less than the threshold
    # Print the solution path
    print('Trying to print solution path...\n')

    if len(solution_path) < SOLUTION_PATH_THRESHOLD:

        print("Solution Path (A*):")

        for i in reversed(solution_path):
            printstate(i)
            print("\n")
    else:
        print(f'Solution len exceeds {SOLUTION_PATH_THRESHOLD}, abort printing states to avoid performance issues')

# main
if __name__ == '__main__':

    # THE START STATE

    # eg start
    # user types: 7 2 4 5 0 6 8 3 1, then start becomes
    start = list(map(int, input("Enter the start state matrix \n").split()))

    # THE GOAL STATE
    # eg goal
    # user types: 0 1 2 3 4 5 6 7 8
    goal = list(map(int, input("Enter the goal state matrix \n").split()))

    # start the timer
    st = time()

    # call the A* search algorithm
    solution = a_star(start, goal, len(start))

    # stop the timer
    et = time()

    # PRINTING RESULT
    print("Execution Time for A*:", et - st, "seconds")
    print()
    print_solution_len(goal)
