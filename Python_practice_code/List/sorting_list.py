"""
sorting_list
"""
#accending order
def lst_sort(lst):

    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return lst

L = [10, 1, 3, 4, 2, 8, 5]
print(lst_sort(L))

#decending order
def lst_sort(lst):

    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] < L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return lst

L = [10, 1, 3, 4, 2, 8, 5]
print(lst_sort(L))
