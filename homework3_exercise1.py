try:
    apple = int(input('How many apples? '))
    students = int(input('How many students? '))
    print(f'Number of apples for each students: {apple//students}. Rest apples in the basket: {apple%students}')

# Error info
except ValueError:
    print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")