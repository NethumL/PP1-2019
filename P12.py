try:
    #Getting the input
    n = int(input("Enter dimension: "))
    p = int(input("Enter p: "))
    if n<=p:
        raise Exception
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))  #Splits at the spaces, and converts all to integers before appending them to "matrix"
        if len(matrix[i]) != n:
            raise Exception

    s = 0  #This will hold the largest sum of submatrices
    num = n-p+1  #The submatrices of size pxp start from the beginning to this index of the matrix

    largest = []  #This list holds the submatrices with the largest sum
    for i in range(1, num):  #These two for loops iterate through the indices from which the submatrices of size pxp start
        for j in range(1, num):
            submatrix = [matrix[i+k][j:j+p] for k in range(p)]  #Gets the submatrix

            mat_sum = sum([sum(row) for row in submatrix])  #Gets the sums of each row into a list, then gets the sum of that list(which will give the sum of the matrix)

            if mat_sum>s:  #If this submatrix has a larger sum
                largest = [submatrix]
            elif mat_sum==s:  #If the sum of this submatrix is the same size as the current largest
                largest.append(submatrix)

    #Getting the output
    for i in range(len(largest)):
        for row in largest[i]:  #Prints the matrix row by row
            print(" ".join(list(map(str, row))))  #Converts all to strings so that the join function will work
        if i<len(largest)-1:  #If there are more matrices to output, then this creates the new line to separate them
            print()
except ValueError:  #If the input contains anything other than integers
    print("Input must only contain integers")
except Exception:  #If either the number of columns doesn't match, or if n is not larger than p
    print("Invalid input")