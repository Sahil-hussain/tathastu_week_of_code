# program for find  second maximum value in dictionarysize

size = int(input(" Enter the no  of items you want to add in dictonary: "))
diction = dict()
for i in range(size):
    key = input(" Enter the key for item " + str(i + 1) + " in dictonary: ")
    value = int(input(" Enter the value for item " + str(i +1) + " in dictonary:"))
    diction[key] = value

print(" The second largest value in the dictonary is",list(sorted(diction.values()))[-2])
