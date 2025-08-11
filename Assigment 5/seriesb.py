n = int(input("Enter the number N:"))

total_sum = 0

for i in range (1,n+1):

    total_sum+=n**i

    print(f"sum of series  N + N^2 + N^3 + ... + N^N is:",total_sum)