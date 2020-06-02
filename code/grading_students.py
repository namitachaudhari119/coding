def grading_students(grades):
    for grade in grades:
        if grade >= 38:
            if grade % 5 == 3:
                grade += 2
            elif grade % 5 == 4:
                grade += 1
            print(grade)
    return grade


grading_students([73, 67, 38, 33])
# grading_students([37, 38])
