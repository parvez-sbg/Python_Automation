#List_intersection
def intersection(lst1, lst2):
    new_lst = []
    for x in lst1:
        if x in lst2:
            new_lst.append(x)
    return new_lst





# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))