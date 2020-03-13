"""Encoding question"""

try:
    #Generates and stores the alphabet into a list
    alphabet = [chr(i) for i in range(97, 123)]

    message = input()
    message = message.replace(" ", "")  #Removes the spaces in the message

    if len(message)<25:
        message = message + "".join(alphabet[:25-len(message)])  #Adds characters from the alphabet to make it up to 25
    elif len(message)>25:  #If the message is too long
        raise Exception

    grid = [[""]*5 for i in range(5)]  #Generates an empty matrix

    c = 0  #The index of the character currently being considered
    i = 2  #The row number of the position being considered
    j = 2  #The column number of the position being considered
    d = 0  #the direction that we're moving in (0 is right, 1 is up, 2 is left, and 3 is down)

    #The steps taken go in the pattern 1,1,2,2,3,3,4,4...
    old = ""  #The number of steps takes in the previous iteration
    new = 1  #The number of steps being taken in the previous iteration
    grid[2][2] = message[c]
    while c<25:  #Breaks out of the while loop once the grid has been filled
        for n in range(new):
            c += 1
            if c==25:  #Breaks out of the for loop once the grid has been filled
                break
            if d==0:
                j += 1
            elif d==1:
                i -= 1
            elif d==2:
                j -= 1
            else:
                i += 1
            grid[i][j] = message[c]
        if new==old:  #If the number of steps taken this time is the same as last time, then next time, one more step has to be taken
            new += 1
        else:  #If the number of steps taken this time is not the same as last time, then next time, the same number of steps has to be taken(so "new" doesn't change)
            old = new
        if d<3:  #Changes the direction for next time
            d += 1
        else:  #If the last direction moved in is down, then the next direction is right
            d = 0

    result = ""
    for row in grid:  #Takes each row, joins them, then joins each row
        result += "".join(list(map(str, row)))

    print(result)
except Exception:  #If there are more characters than 25(without spaces)
    print("Input has too many characters")