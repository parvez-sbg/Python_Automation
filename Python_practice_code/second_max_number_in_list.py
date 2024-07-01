# find the secodn max number in a list
def second_max(List):
    max_1 = List[0]
    max_2 = List[0]

    for i in range(len(List)):
        if List[i] > max_1:
            max_1 = List[i]

    for i in range(len(List)):
        if List[i] > max_2 and List[i] < max_1:
            max_2 = List[i]
    return max_2
