listOne = []
listTwo = []
x = 0

while x < 5:
    value = int(input(print('Enter a number for the first list: ')))
    listOne.append(value)
    x = x + 1

x = 0

while x < 5:
    value = int(input(print('Enter a number for the second list: ')))
    listTwo.append(value)
    x = x + 1

print(set(listOne).intersection(listTwo))