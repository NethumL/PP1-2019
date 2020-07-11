"""Isograms question"""

try:
    text = input().lower()

    valid = False  #Whether the text is an isogram
    for char in text:
        if char.isalpha():  #Checks if the current character is a letter
            if text.count(char)>1:  #Checks if it has repeated
                break
    else:
        valid = True

    if valid:
        print("This is an isogram")
    else:
        print("This is not an isogram")
except:
    print("Invalid Input")