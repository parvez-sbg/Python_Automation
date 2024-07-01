#merge_of_two_sorted_list:
def merge_lists(lst1, lst2):
    new_lst1 = sorted(lst1)
    new_lst2 = sorted(lst2)
    lst3 = sorted(new_lst2 + new_lst1)

    return lst3

#driver code:
lst1 = [10,929, 92, 90, 2, 1]
lst2 = [100, 30, 290,1000]
print(merge_lists(lst1, lst2))