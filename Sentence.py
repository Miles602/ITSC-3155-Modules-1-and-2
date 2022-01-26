myList = []
sentence = (' ')
x = 0

while x < 5:
    word = input(print('Enter a word: '))
    sentence += ('{} '.format(word))
    x = x + 1

print(sentence)