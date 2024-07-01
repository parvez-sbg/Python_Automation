# Reverse a list:

def lst_reverse(lst):
    new_list = []
    for i in range(len(lst)):
        new_list.append(lst[-1-i])
    return new_list

lst = ["apple", "ball", "cat", "Dog"]
print(lst_reverse(lst))
