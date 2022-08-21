# Importing the dependencies
from time import time

# CONSTANT
SOLUTION_PATH_THRESHOLD = 300

# This utility function is used to print the state.
def printstate(state):
    print("State: ");
    n = len(state)
    N = int(n ** 0.5)
    for i in range(N):
        print(' '.join(map(str, state[i * N:(i + 1) * N])))
    print('*'*20)
    return ""

# This function generates the children of the given state.
def generate_children(state):

    # The children are stored in a list.
    children = []

    # The number of tiles is obtained.
    n = len(state)

    # The number of rows and columns is calculated.
    N = int(n ** 0.5)

    # The blank tile is found.
    zero_index = state.index(0)

    # The row and column of the blank tile is calculated.
    row = zero_index // N
    col = zero_index % N

    # The children are generated.
    for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:

        # If the child is valid, it is added to the children list.
        if 0 <= i < N and 0 <= j < N:

            # swap the position of the blank space with the position of the tile
            zero_index = state.index(0)
            temp = state[i * N + j]
            state[i * N + j] = state[zero_index]
            state[zero_index] = temp

            # add the child to the children list
            children.append(state.copy())

            # swap the position of the blank space with the position of the tile
            # back to its original position
            temp = state[i * N + j]
            state[i * N + j] = state[zero_index]
            state[zero_index] = temp

    # The children are returned.
    return children

# This function is used to solve the puzzle. It takes the initial state and the goal state as input
# and returns the solution state.
def solve(initial, goal):

    # The queue is used to store the states that are yet to be explored.
    queue = []

    # The visited dict is used to store the states that have been explored.
    visited = {}

    # The initial state is added to the frontier.
    queue.append(initial)
    visited[str(initial)] = None

    # While the frontier is not empty, we keep on exploring the states.
    while queue:
        # The current state is the first state in the frontier.
        current_state = queue[0]
        queue.pop(0)

        # If the current state is the goal state, we return the solution path.
        if current_state == goal:
            return visited

        # The children of the current state are generated.
        children = generate_children(current_state)

        # The children are added to the frontier if they are not already present in the frontier or
        # in the explored set.
        for child in children:
            if str(child) not in visited:
                queue.append(child)
                visited[str(child)] = current_state

    # If the frontier is empty, then the puzzle cannot be solved.
    return None


# This function is used to print the solution path.
def print_solution(solution, parent):

    solution_path = []

    # Tracing the goal state to the start state path
    while str(solution) in parent.keys():
        solution_path.append(solution)
        solution = parent[str(solution)]

    print(f"Length of solution_path (BFS): {len(solution_path)}\n")

    # If the solution path is less than the threshold
    # Print the solution path
    print('Trying to print solution path...\n')

    if len(solution_path) < SOLUTION_PATH_THRESHOLD:

        print("Solution Path (BFS):")

        for i in reversed(solution_path):
            printstate(i)
            print("\n")
    else:
        print(f'Solution len exceeds {SOLUTION_PATH_THRESHOLD}, abort printing to avoid performance issues')

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

    # solve the puzzle
    visited = solve(start, goal)

    # stop the timer
    et = time()

    # PRINTING RESULT
    print("Execution Time for BFS:", et - st, "seconds")

    if visited is None:
        print("No solution found!")

    else:

        # The solution path is printed.
        print_solution(goal, visited)
