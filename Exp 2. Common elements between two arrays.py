nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]

answer1 = 0
answer2 = 0

for i in nums1:
    if i in nums2:
        answer1 += 1

for i in nums2:
    if i in nums1:
        answer2 += 1

print([answer1, answer2])