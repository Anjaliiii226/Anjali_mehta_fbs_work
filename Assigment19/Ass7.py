num = [i for i in range(1, 1001) if any(i % div == 0 for div in range(2, 10))]
print(num)
