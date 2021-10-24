# я пока не разобрался, как корректно тестировать функцию с декоратором.

# import unittest
#
# from homework5.task02 import custom_sum, print_result
#
#
# class TestTask02Func(unittest.TestCase):
#
#     def setUp(self):
#         self.custom_sum = custom_sum
#
#     # custom_sum([1, 2, 3], [4, 5])
#     # custom_sum(1, 2, 3, 4)
#     def tests(self):
#         assert custom_sum.__doc__ ==
#         'This function can sum any objects which have __add___'
#         assert custom_sum.__name__ == 'custom_sum'
#         assert custom_sum.__original_func ==
#         '<function custom_sum at <some_id>>'

# the result returns without printing
# print(custom_sum.__doc__)
# 'This function can sum any objects which have __add___'
# print(custom_sum.__name__)
# 'custom_sum'
# print(custom_sum.__original_func)
# <function custom_sum at <some_id>>
