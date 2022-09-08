try:
    classroomA = int(input('How many students in classroom A? '))
    classroomB = int(input('How many students in classroom B? '))
    classroomC = int(input('How many students in classroom C? '))

# modulo operation (rest student from each classroom need desk)
    rest = classroomA%2 + classroomB%2 + classroomC%2

    print('Number of desks for students:', classroomA // 2 + classroomB // 2 + classroomC // 2 + rest)

# Error info
except ValueError:
    print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")
