student_name = input()
reached_grade = 1
sum_grades = 0
excluded = 0

while reached_grade <= 12:
    current_grade = float(input())
    if current_grade < 4:
        excluded += 1
        if excluded > 1:
            break
        continue
    sum_grades += current_grade
    reached_grade += 1

average_grade = sum_grades /12

if excluded >= 2:
    print(f'{student_name} has been excluded at {reached_grade} grade')
else:
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
