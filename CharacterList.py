characterList = list(input(print('Enter a string: ')))
myList = []
lastList = []
x = 0
count = 0
n = 0

setLengthList = int(len(characterList) / 3)
setLength = len(characterList)

for i in range (int(len(characterList) / 3)):
    myList.append([])

while x < setLength:
    myListItem = characterList[0]
    myList[n].append(myListItem)

    characterListItem = characterList[0]
    characterList.remove(characterListItem)
    count = count + 1

    if (count == 3):
        if (n == setLengthList - 1 and len(myList[n]) == 3):
            for z in characterList:
                lastList.append(z)

            myList.append(lastList)
            x = setLength
        else:
            n = n + 1
        count = 0


    x = x + 1


print (myList)