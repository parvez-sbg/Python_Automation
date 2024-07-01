"""remove_duplicate_list"""
def remove_duplicates(lst):
    duplicate_removed_list = []
    for element in lst:
        if element not in duplicate_removed_list:
            duplicate_removed_list.append(element)
    return duplicate_removed_list



lst = ["Maisha", "Parvez", "rahib", "Maisha", "Parvez", "apple"]
print("New list:",remove_duplicates(lst))