"""Minimax algorithm"""

try:
    r, c = map(int, input().split())
    matrix = []
    for i in range(r):
        row = list(map(int, input().split()))
        if len(row) != c:
            raise Exception
        matrix.append(row)

    #Finding maximin
    mins = []  #A list of the minimums in the rows
    for row in matrix:
        mins.append(min(row))
    maximin = max(mins)  #Gets the max of the row minimums

    #Finding minimax
    maxes = []  #A list of the maximums in the columns
    for i in range(c):
        column = [matrix[j][i] for j in range(r)]  #Gets the current column into a list
        maxes.append(max(column))
    minimax = min(maxes)  #Gets the min of the column maximums

    if minimax==maximin:
        state = "deterministic"
    else:
        state = "probabilistic"

    print("This games is", state)
except ValueError:
    print("Input must only contain integers")
except Exception:
    print("The number of rows and columns must match the input")