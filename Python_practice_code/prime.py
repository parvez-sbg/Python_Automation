#Write a program to find if the given number is prime or not.

num = int(input("enter a number to check whether it is prime or not:"))

if num <= 1:
    print("{} is not a prime number".format(num))
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print("{} is a prime number.".format(num))
    else:
        print("{} is not a prime number.".format(num))

""" prime number in a list """


