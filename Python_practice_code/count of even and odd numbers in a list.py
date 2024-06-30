# count of even and odd numbers in a list:
def count_even_numbers(lst):
    count_even = 0


    for num in lst:
        if num % 2 == 0:
            count_even = count_even + 1
    return count_even


lst = [1, 2, 20, 37, 30, 32, 60, 65, 77]
print(count_even_numbers(lst))
odd_number = len(lst) - count_even_numbers(lst)
print(odd_number)