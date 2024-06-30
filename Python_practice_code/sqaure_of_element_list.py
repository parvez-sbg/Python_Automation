# sqaure_of_element_list
def sqaure_elements_list(lst):
    square = [x**2 for  x in lst ]
    return square

#driver code
lst = [1,2,3,4,2,22,1,3,4]
print(sqaure_elements_list(lst))