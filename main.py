assignment_1 = float(input('Enter assignment 1 grade (0-100): '))
assignment_2 = float(input('Enter assignment 2 grade (0-100): '))
assignment_3 = float(input('Enter assignment 3 grade (0-100): '))
assignment_4 = float(input('Enter assignment 4 grade (0-100): '))

test_1 = float(input('Enter test 1 grade (0-100): '))
test_2 = float(input('Enter test 2 grade (0-100): '))

grade_total = ((round(assignment_1 * .1125))
               + (round(assignment_2 * .1125))
               + (round(assignment_3 * .1125))
               + (round(assignment_4 * .1125))
               + (round(test_1 * .275))
               + (round(test_2 * .275)))


result = f'Final grade: {grade_total/100:.2f}'
print(result, end=' ')

if grade_total < 60:
    print('F', end=' ')
if 60 < grade_total < 70:
    print('D', end=' ')
if 69 < grade_total < 80:
    print('C', end=' ')
if 79 < grade_total < 90:
    print('B', end=' ')
if 89 < grade_total <= 100:
    print('A', end=' ')





