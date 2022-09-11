#!/usr/bin/env python

### FizzBuzz 

number1 = input("Enter a number from 1 to 10000: ")
number2 = input("Enter a second numer 1 to 10000: ")

## check if input is numeric:
if number1.lstrip('-').isnumeric() and number2.lstrip('-').isnumeric():
    ## define variables as integers:
    n = int(number1)
    m = int(number2)
    ## check if input is in range:
    if (1 <= n <= 10000) and (1 <= m <= 10000):
        if (n < m): 
            for i in range(n, m+1): ## for inclusive values
                    if i % 3 == 0 and i % 5 == 0:
                        print("FizzBuzz")
                    elif i % 3 == 0:
                        print("Fizz")
                    elif i % 5 == 0:
                        print("Buzz")
                    else:
                        print(i)
        else:
            print("Second number must be higher than the first one")
    elif (1 > n < 10000):
        print("First number is out of range")
    else:
        print("Second number is out of range")
elif number2.lstrip('-').isnumeric():
    print("First number is not numeric")
elif number1.lstrip('-').isnumeric():
    print("Second number is not numeric")
else:
    print("Input is not numeric")

