# 4 methods to count the appearance of a substring in a given string.
import re


# method 1: 'in' operator
def count_substring_method_1(s, sub):
    if sub in s.strip().lower():
        return True
    else:
        return False


# method 2: find()
def count_substring_method_2(s, sub):
    index = s.strip().lower().find(sub)
    if index != -1:
        return True
    else:
        return False


# Method 3: re
def count_substring_method_3(s, sub):
    if re.search(sub, s.strip().lower()):
        return True
    else:
        return False


# Method 4: count
def count_substring_method_4(s, sub):
    if s.strip().lower().count(sub) > 0:
        return True
    else:
        return False


main_string = "Hello, how are you?"
substring = "how"
print(count_substring_method_1(main_string, substring))
print(count_substring_method_2(main_string, substring))
print(count_substring_method_3(main_string, substring))
print(count_substring_method_4(main_string, substring))
