#dict_of_tupple_list
tuple_list = [("a", 1), ("b", 2), ("c", 3)]
d = {}

new_list1=[]
new_list2 = []
for i in range(len(tuple_list)):
    new_list1.append(tuple_list[i][0])
    new_list2.append(tuple_list[i][1])

for i in range(len(tuple_list)):
    d1 = {new_list1[i]:new_list2[i]}
    d.update(d1)

print(new_list1)
print(new_list2)
print(d)
