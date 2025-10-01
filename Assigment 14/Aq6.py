def pair(nums):
    num_set = set(nums)
    nums = sorted(num_set)


    prod1 = nums[-1] * nums[-2]

    prod2 = nums[0] * nums[1]


    if prod1 >= prod2:
        return (nums[-2], nums[-1]), prod1
    else:
        return (nums[0], nums[1]), prod2

set = [3, 5, -10, -20, 7, 6]
pair, product = pair(set)
print("Pair with maximum product:", pair)
print("Maximum product:", product)