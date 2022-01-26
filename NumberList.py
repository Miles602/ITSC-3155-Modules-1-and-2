myList = []
key = 'QUIT'
num = input(print('Enter a number or QUIT to quit: '))

while (num != key):
    num = int(num)
    myList.append(num)
    num = input(print('Enter a number or QUIT to quit: '))

if(num == key):
    print(myList)
