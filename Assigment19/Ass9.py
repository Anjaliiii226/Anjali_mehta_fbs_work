def palindrome():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1

num = palindrome()

for _ in range(30):
    print(next(num), end=" ")
