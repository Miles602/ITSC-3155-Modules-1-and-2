gradeValue = input("Enter a grade from 0 to 100: ")
gradeValue = int(gradeValue)

if (gradeValue > 100):
    print(f'INVALID: You entered a value over 100')
if (gradeValue < 0):
    print(f'INVALID: You entered a value below 0')

if (gradeValue > 89 and gradeValue <= 100):
    print(f'Your grade is A')
if (gradeValue > 79 and gradeValue < 90):
    print(f'Your grade is B')
if (gradeValue > 69 and gradeValue < 80):
    print(f'Your grade is C')
if (gradeValue > 59 and gradeValue < 70):
    print(f'Your grade is D')
if (gradeValue >= 0 and gradeValue < 60):
    print(f'Your grade is F')