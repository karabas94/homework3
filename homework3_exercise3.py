try:
    n = int(input('Enter of number: '))
    print("Reverse number: ", n%10,(n%100)//10,n//100, sep='')

# Error info
except ValueError:
    print("Do not enter letters or symbols. Please, restart the program and enter NUMBER")
