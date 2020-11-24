"""Burrows-Wheeler Transformation"""


try:
    #Getting the inputs
    text = input()

    #Checking whether only A, C, G, and T are there in the text
    for char in text:
        if char not in ["A", "C", "G", "T"]:
            raise Exception

    #Adding the $ sign to the end
    text = text + "$"

    #Getting the permutations
    perm = [text]  #Initializes the list of permutations with the original
    for _ in range(len(text)-1):
        perm.append(perm[-1][-1] + perm[-1][:-1])  #Attaching the last character in the previous permutation to the beginning

    #Sorting the permutations
    perm.sort()

    #Printing out the BWT
    for i in perm:
        print(i[-1], end = "")
    print()  #Moves the cursor to the next line(Not essential)
except Exception:
    print("Input must contain only A, C, G, and T")