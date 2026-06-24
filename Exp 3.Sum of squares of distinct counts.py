nums = list(map(int, input("Enter array elements: ").split()))

total = 0

for i in range(len(nums)):
    s = set()

    for j in range(i, len(nums)):
        s.add(nums[j])

        distinct_count = len(s)

        total += distinct_count * distinct_count

print("Sum of squares of distinct counts:", total)