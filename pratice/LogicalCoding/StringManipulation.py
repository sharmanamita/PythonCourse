def reverse_String(s):
    return s[::-1]


def find_largest(numbers):
    return max(numbers) if numbers else None


def find_smallest(numbers):
    return min(numbers) if numbers else None


def find_2nd_largest(numbers):
    return sorted(numbers, reverse=True)[1] if numbers else None


def palindrome(s):
    return s == s[::-1]


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def check_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


print(reverse_String("Hello World"))
print("largest:", find_largest([14, 42, 53, 41, 45]))
print("smallest:", find_smallest([14, 42, 53, 41, 45]))
print("2nd largest:", find_2nd_largest([14, 42, 53, 41, 45]))
print(palindrome("madam"))
print(palindrome("hello"))
print(count_vowels("Namita Sharma"))
print("Is s1, s2 = listens, silent are anagram: ", check_anagram("listen", "silent"))
