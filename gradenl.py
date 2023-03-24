# initialize an empty list to store students and grades
students = []
# take input of name and grade for each student
for i in range(int(input())):
    name = input()
    grade = float(input())
    students.append([name, grade])

# sort the list in ascending order based on the grades
sorted_grades = sorted(students, key=lambda x: x[1])

# find the second lowest grade
second_lowest_grade = None
for i in range(1, len(sorted_grades)):
    if sorted_grades[i][1] != sorted_grades[0][1]:
        second_lowest_grade = sorted_grades[i][1]
        break

# find and print the names of students with the second lowest grade
students_with_second_lowest_grade = []
for student in sorted_grades:
    if student[1] == second_lowest_grade:
        students_with_second_lowest_grade.append(student[0])

# sort and print the names in alphabetical order
students_with_second_lowest_grade.sort()
for student_name in students_with_second_lowest_grade:
    print(student_name)

