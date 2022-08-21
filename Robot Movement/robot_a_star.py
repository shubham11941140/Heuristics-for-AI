# Importing Dependencies
from heapq import heappush, heappop
import sys
from time import time

# CONSTANTS
SOLUTION_PATH_THRESHOLD = 300

# This dictionary to store parent of child states and marks the visited states
visited = dict()

# Gets the possible moves from the state
def get_moves(state, graph):

    height = len(graph)
    width = len(graph[0])

    moves = []

    x, y = state

    for i, j in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
        if 0 <= i < height and 0 <= j < width and graph[i][j] == 0:
            moves.append((i, j))

    return moves

# This function calculates heuristic cost for each tile in a state
# Manhattan distance is used to calculate the heuristic cost
def heuristic(state, goal):
    row, col = state
    final_row, final_col = goal
    return abs(row - final_row) + abs(col - final_col)

# This function implements the A* search algorithm
def a_star(start, goal, graph):

    # Create a priority queue
    pq = []

    # Push the initial state to the priority queue
    heappush(pq, (heuristic(start, goal), start))

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
        moves = get_moves(state, graph)

        # For each move
        for move in moves:

            # Push the move to the priority queue if not visited
            if str(move) not in visited.keys():

                # Mark the move as visited by setting the parent of the move as the current state
                visited[str(move)] = state
                heappush(pq, (heuristic(move, goal), move))

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
            print(i)
    else:
        print(f'Solution len exceeds {SOLUTION_PATH_THRESHOLD}, abort printing states to avoid performance issues')

# main
if __name__ == '__main__':

    graph = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,0],
        [1,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]

    height = len(graph)
    width = len(graph[0])

    # THE START STATE
    start = tuple(map(int, input("Enter Start:").split()))

    # THE GOAL STATE
    goal = tuple(map(int, input("Enter Goal:").split()))

    if graph[start[0]][start[1]] == 1 or graph[goal[0]][goal[1]] == 1:
        print("Invalid Input! The start or goal state cannot be a blocked cell.")
        sys.exit()

    # start the timer
    st = time()

    # call the A* search algorithm
    solution = a_star(start, goal, graph)

    # stop the timer
    et = time()

    # PRINTING RESULT
    print("Execution Time for A*:", et - st, "seconds")
    print()
    print_solution_len(goal)
