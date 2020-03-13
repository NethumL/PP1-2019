"""Adjacency matrix question"""

try:
    n = int(input())

    inputs = input().split()

    matrix = [[0]*(n+1) for i in range(n+1)]
    matrix[0][0] = " "

    #Labelling the rows and columns
    for i in range(n):
        matrix[0][i+1] = i+1
        matrix[i+1][0] = i+1
    
    #Counting the edges
    for pair in inputs:
        a, b = map(int, pair.split(","))
        matrix[a][b] += 1

    #Getting the output
    sep = "+-"*(n+1) + "+"  #Creating the formatting
    for row in matrix:
        print(sep)
        print("|" + "|".join(list(map(str, row))) + "|")
    print(sep)  #Closing the end of the output with the formatting
except:
    print("Invalid Input")