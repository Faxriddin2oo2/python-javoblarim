# Bismillah
"""
Created on Thu Aug  8 22:20:50 2024

@author: Faxriddin
"""


# # String to Integers.
# def convert_add(lst):
#     sonlar = [int(son) for son in lst]
#     return sum(sonlar)

# print(convert_add(["1", '2', "4"]))


# Username Generator

# import random as r

# ReversedName = []
# def user_name(name):
#     for i in reversed(name.lower()):
#         ReversedName.append(i)
#     return ''.join(ReversedName) + str(r.randint(1, 10))

# print(user_name('vali'))


# def get_name_by_number(file_path, number):
#     with open(file_path) as file:
#         for line in file:
#             if line.startswith(f'#{number} -'):
#                 return line
#     return None

# file_path = 'hayot_yoli.txt'
# number = 6
# result = get_name_by_number(file_path, number)
# if result:
#     print(result)
# else:
#     print(f'Имя с номером {number} не найдено.')

# Given an integer x, return true if x is a palindrome, and false otherwise.
# An integer is a palindrome when it reads the same forward and backward. For example, 121 is a palindrome while 123 is not.
# class Solution(object):
#     def isPalindrome(self, x):
#         number = []
#         for n in reversed(str(x)):
#             number.append(n)
#         y = ''.join(number)
#         if str(x) == y:
#             return 'true'
#         else:
#             return 'false'
# print(Solution.isPalindrome(-121))

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        str_x = str(x)
        
        return str_x == str_x[::-1]

solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10)) 