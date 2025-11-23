import threading

results = [0, 0, 0, 0]

def sum_of_squares(start, end, index):
    total = 0
    for i in range(start, end + 1):
        total += i * i
    results[index] = total

ranges = [
    (1, 25),
    (26, 50),
    (51, 75),
    (76, 100)
]

threads = []

for i, (start, end) in enumerate(ranges):
    t = threading.Thread(target=sum_of_squares, args=(start, end, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

total_sum = sum(results)

print("Partial sums from each thread:", results)
print("Total sum of squares from 1 to 100:", total_sum)
