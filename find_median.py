# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/25/2024
# Description: Define a function named 'find_median' that takes
# as a parameter a list of numbers.

def find_median(num):
    """
    Returns None if there's no number
    :param num: list of values
    :return: None if no values entered or median value of list
    """
    if not num:
        return None

    num.sort()

    n = len(num)
    if n % 2 == 1:
        median = num[n // 2]
    else:
        left_middle = num[n // 2 - 1]
        right_middle = num[n // 2]
        median = (left_middle + right_middle) / 2

    return median

# Test 1: Five integers
# list1 = [49, 16, 8, 49]
# print(find_median(list1))
# Result: 32.5

# Test 2: Three floats
# list2 = [8.5, -2, -5]
# print(find_median(list2))
# Result: -2

# Test 3: Empty
# list3 = []
# print(find_median(list3))
# Result: None