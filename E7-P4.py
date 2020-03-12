try:
    p, q = map(int, input().split())  #Takes the inputs, converts them to integers, and assigns them to the variables

    if p>=q:  #If p is larger
        print("p must be smaller than q")
    elif p<0:  #If at least one of them is negative
        print("p and q must be positive")
    else:
        result = 0  #Count of the stepping numbers
        for num in range(max(p,10), q+1):  #The larger of p and 10 has to be taken as the starting number, as 1-digit numbers can't be stepping numbers
            num = list(map(int, str(num)))  #Creates a list of the digits
            for i in range(len(num)-1):
                if abs(num[i]-num[i+1]) != 1:  #Checks whether the gap is 1
                    break
            else:  #This block is only executed if the break statement wasn't executed, i.e. the gap between all consecutive digits is 1
                result += 1

        print(result)
except ValueError:  #If the input contains anything other than integers
    print("Inputs must be two integers")