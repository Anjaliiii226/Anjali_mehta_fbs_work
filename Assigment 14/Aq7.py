def missing(set1, set2):

    set2 = set1.difference(set2)

    set1 = set2.difference(set1)

    return set2, set1


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set2, set1 = missing(set1, set2)

print("Numbers in set1 but not in set2:", set2)
print("Numbers in set2 but not in set1:",set1)