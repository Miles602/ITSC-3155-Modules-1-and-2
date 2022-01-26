wordOne = input('Enter a string: ')
wordTwo = input('Enter another string: ')

if (wordOne in wordTwo):
    print(f'True')
elif (wordTwo in wordOne):
    print(f'True')
elif (wordOne not in wordTwo):
    print(f'False')
elif (wordTwo not in wordOne):
    print(f'False')