# def my_gen():
#     n = 1
#     print("This is printed first")
#
#     yield n
#     n += 1
#     print("This is printed second")
#
#     yield n
#     n += 1
#     print("Printed third")
#     yield n
#
#
# for item in my_gen():
#     print(item)

# def square_numbers(nums):
#     for i in nums:
#         yield i*i
#
#
# my_nums = square_numbers([1, 2, 3, 4, 5])
# for num in my_nums:
#     print(num)
#

my_nums = (x*x for x in [1, 2, 3, 4, 5])
for num in my_nums:
    print(num)
    