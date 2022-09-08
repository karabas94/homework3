try:
    n = int(input('Enter of number: '))
    first = n%10
    second = (n%100)//10
    third = n//100
    final = (first*100+second*10+third)
    print(f'Reverse number: {final}')

# Error info
except ValueError:
    print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")
