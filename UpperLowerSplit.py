userString = input('Enter a string: ')
characterList = []
outputList = []

for x in userString:
    characterList.append(x)

for z in characterList:
    if(z.islower()):
        outputList.append(z)

for c in characterList:
    if(c.isupper()):
        outputList.append(c)    

print(*outputList, sep='')
