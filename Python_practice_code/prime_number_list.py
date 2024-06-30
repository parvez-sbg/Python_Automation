#To find the number of prime number in a list
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def check_prime(lst):
    prime_numbers = []
    for num in lst:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Original list:", numbers)
prime_numbers = check_prime(numbers)
print("Prime numbers in the list:", prime_numbers)