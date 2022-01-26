myList = []
newList = []
x = 0
counter = 1
savedValue = 0

while x < 10:
    value = int(input(print('Enter a number: ')))
    myList.append(value)
    x = x + 1

if (len(set(myList)) == len(myList)):
    print (myList)
else:
    myList.sort()

    while savedValue < len(myList) - 1:
        if (myList[savedValue] == myList[counter]):
            num = myList[savedValue]

            try:
                while True:    
                    myList.remove(num)
            except ValueError:
                pass

            savedValue = savedValue
        else:
            savedValue = savedValue + 1

            if (counter == len(myList) - 1):
                counter = counter
            else:
                counter = counter + 1

    print(myList)