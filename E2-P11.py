"""Sum of elements in sub-square matrices"""

try:
    #Getting the inputs n, p, and q
    n = int(input("Enter dimension: "))
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))

    #Taking the matrix as an input
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))  #Splits by spaces, converts all to integers, then appends to "matrix"
        if len(matrix[i]) != n:  #If the length of the rows doesn't match the expected number of columns
            raise Exception
    
    if (1>p) or (p>q) or (q>n):  #If the conditions for p, q, and n are not satisfied
        raise Exception

    result = 0  #Will contain the sums of all the square submatrices
    for s in range(p, q+1):  #Iterates through the sizes of square submatrices
        t = n-s+1  #This is the index until which square submatrices of size "s" start
        for i in range(t):  #Iterate through the indices where the square submatrices start
            for j in range(t):
                submatrix = [matrix[i+k][j:j+s] for k in range(s)]  #Gets the submatrices by going row by row, and using list comprehensions to create the 2-dimensional array
                tot = sum([sum(row) for row in submatrix])  #Gets the sums for each row, and puts them into a list, and then it takes the sum of that list, which gives the sum of the matrix
                result += tot

    #Getting the output
    print(result)

except ValueError:  #If the input has anything other than integers
    print("Input must only contain integers")

except Exception:
    print("Invalid Input")