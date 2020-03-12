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
    maximin = 0
    for row in matrix:
        maximin = max(maximin, min(row))  #Takes the larger of the current maximin and the minimum of the current row

    #Finding minimax
    maxes = []  #A list of the maxes in the columns
    for i in range(c):
        column = [matrix[j][i] for j in range(r)]  #Gets the current column into a list
        maxes.append(max(column))
    minimax = min(maxes)

    if minimax==maximin:
        state = "deterministic"
    else:
        state = "probabilistic"

    print(maximin, minimax)
    print(maxes)

    print("This games is", state)
except ValueError:
    print("Input must only contain integers")
except Exception:
    print("The number of rows and columns must match the input")