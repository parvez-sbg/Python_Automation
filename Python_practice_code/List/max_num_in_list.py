# Function to find the maximum number in a list.

def max_number(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:

            max_num = num
    return max_num

lst = [83, 73, 100, 89,3773, 888]


print(max_number(lst))