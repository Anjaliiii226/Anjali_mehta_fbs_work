set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

diff1 = set1.difference(set2)

diff2 = set2.difference(set1)

print("Elements in set1 but not in set2:", diff1)
print("Elements in set2 but not in set1:", diff2)