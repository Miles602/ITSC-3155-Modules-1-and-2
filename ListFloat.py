size = int(input('Enter a number: '))
myList = []
x = 0
y = 1
average = 0

while x < size:
    inputList = float(input('Enter number {}: '.format(y)))
    myList.append(inputList)
    x = x + 1 
    y = y + 1

x = 0

while x < size:
    average = average + myList[x]
    x = x + 1

average = average / size

print('List: {}'.format(myList))
print('Average: {}'.format(average))