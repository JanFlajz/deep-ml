def create_unique_set(list1: list)-> set:
    unique =set()
    for l in list1:
        if l in unique:
            unique.remove(l)
        else:
            unique.add(l)
    return unique

def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer
    
    unique1 = create_unique_set(list1)
    unique2 = create_unique_set(list2)
    return len(unique1 & unique2)