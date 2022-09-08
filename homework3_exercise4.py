try:
    n = int(input('Enter seconds: '))
# floor division operation (integers of hours)
    hours = n//3600
# modulo operation (rest seconds form hours)
    rests = n%3600
# floor division operation (integers of min)
    min = rests//60
# modulo operation (rest seconds from minutes)
    sec = rests%60

    print(f'Time: {hours}:{min}:{sec}')

# Error info
except ValueError:
    print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")
