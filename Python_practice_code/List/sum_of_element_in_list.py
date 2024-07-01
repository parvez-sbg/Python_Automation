# Sum of elements in a list:

def sum_of_elements(lst):
    sum = 0
    for num in lst:
        sum = sum + num
    return sum


lst = [1, 20, 20, 50, 100]
print(sum_of_elements(lst))