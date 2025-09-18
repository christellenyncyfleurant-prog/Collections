def calculate_grade(grade):
    average = (grade[0] + grade[1] + grade[2] + grade[3] + grade[4] ) / 5

    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    return average, letter

name = input("What is the student's name? ")
grade = []
grade.append(int(input("Enter the first grade: ")))
grade.append(int(input("Enter the second grade: ")))
grade.append(int(input("Enter the third grade: ")))
grade.append(int(input("Enter the fourth grade: ")))
grade.append(int(input("Enter the fifth grade: ")))

average, letter = calculate_grade(grade)
print("The average is\n", average)
print("Letter Grade: ", letter)
