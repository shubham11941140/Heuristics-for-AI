from collections import Counter
from numpy import array, copy, diag, fliplr

# Store all rows, columns and diagonals of a matrix
def store(a):
    return [a[i, :] for i in range(3)] + [a[:, i] for i in range(3)] + [diag(a)] + [diag(fliplr(a))]

# Count number of 1s in a numpy array
def count(a, val):
    return Counter(a.flatten()).get(val, 0)

def xn(s, n):
    return len([1 for i in store(s) if count(i, 'X') == n and count(i, '0') == 0])

def on(s, n):
    return len([1 for i in store(s) if count(i, 'X') == 0 and count(i, '0') == n])

def score(s):
    return (8 * xn(s, 3) + 3 * xn(s, 2) + xn(s, 1)) - (8 * on(s, 3) + 3 * on(s, 2) + on(s, 1))

# Print Matrix with borders
def print_mat(a):

    for i in range(3):

        print("|", end="")

        for j in range(3):

            print(a[i][j], end = "")

        print("|")

# BFS
# Put X in a tic tac toe and show all possibilities
def bfs(a):

    adj = [0 for _ in range(6)]
    mat = [[] for _ in range(6)]
    queue = [(a, 0)]

    while queue:

        a, level = queue.pop(0)
        mat[level].append(a)
        adj[level] += 1

        if (level + 1) % 2:

            for i in range(3):
                for j in range(3):

                    if a[i][j] == '_':

                        b = copy(a)
                        b[i][j] = 'X'
                        queue.append((b, level + 1))
        else:

            # Put 0
            for i in range(3):
                for j in range(3):

                    if a[i][j] == '_':

                        b = copy(a)
                        b[i][j] = '0'
                        queue.append((b, level + 1))

    return adj, mat

def main():

    state = [['_', 'X', '_'], ['0', '_', '_'], [ 'X', '_', '0']]
    adj, mat = bfs(state)

    for level in range(6):

        print("LEVEL is:", level + 1, "\n")

        print("The Number of Matrices at this level is:", adj[level], "\n")

        for idx, i in enumerate(mat[level]):

            print("The Matrix Number is:", idx + 1)
            print()
            print_mat(i)
            print()
            print("The Score is:", score(array(i)))
            print()

if __name__ == '__main__':
    main()

