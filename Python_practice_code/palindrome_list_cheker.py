#palindrome_list_cheker:
def is_palindrome(lst):
    str_lst = "".join(map(str, lst))

    return str_lst == str_lst[::-1]

numbers1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
numbers2 = [2,2,3,4,3,2,2,4]
print(is_palindrome(numbers1))
print(is_palindrome(numbers2))
