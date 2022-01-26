row, colum = (5, 5)

grid = [[0 for x in range(colum)] for y in range(row)] 

rowNum = int(input(print('Enter a row num from 1 to 5: ')))
columNum = int(input(print('Enter a colum num from 1 to 5')))

if(rowNum >= 1 and rowNum <= 5 and columNum >=1 and columNum <= 5):
    grid[rowNum - 1][columNum - 1] = 1

for item in grid:
    row = (' ')
    for subItem in item:
        row += ('{} '.format(str(subItem)))
    
print (row)