def range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("step cannot be zero")

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

for num in range(2, 10, 2):
    print(num, end=" ")
