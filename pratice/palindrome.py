from math import floor
from numpy import max


def isPalindrome(str: str):
    return str == str[::-1]


print(isPalindrome("namita"))
print(isPalindrome("madam"))
