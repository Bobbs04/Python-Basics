# # list []
# # sum
# lists_1 = [10, 3, 18, 9, 100]
# total = 0
# for lst in lists_1:
#     total += lst
# print(total)
#
# # multiply
# nums = [10, 3, 4]
# total = 1
# for number in nums:
#     total *= number
# print(total)
#
# # largest
# nums = [10, 15, 89, 100, 2, 3, 4, 5]
# max_1 = nums[0]
# for num in nums:
#     if num > max_1:
#         max_1 = num
# print(max_1)
#
# # smallest
# nums = [10, 15, 89, 100, 2, 3, 4, 5]
# min_1 = nums[0]
# for n in nums:
#     if n < min_1:
#         min_1 = n
# print(min_1)


def match_words(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr


print(match_words(['abc', 'xyz', 'aba', '1221']))



