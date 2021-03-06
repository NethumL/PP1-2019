"""Ranking question"""


try:
    inputs = input().split()

    for t in inputs:
        if not t.isalnum():  #Checking if there are any non-alphanumeric characters in the input
            raise ValueError

    #Generates the list of the characters in the order of precedence
    order = [chr(i) for i in range(97, 123)]
    num_order = [str(i) for i in range(10)]
    order += num_order

    result = [""]*len(inputs)
    rank = 0
    for i in order:
        if i in inputs:
            c = inputs.count(i)
            indices = [j for j in range(len(inputs)) if inputs[j]==i]  #Gets a list of the indices that have the character "i"
            for index in indices:
                result[index] = str(rank)  #Assigns all of them the same rank
            rank += len(indices)  #Increments rank by the number of occurrences

    print(" ".join(result))
except ValueError:
    print("Input must only contain alphanumeric characters")