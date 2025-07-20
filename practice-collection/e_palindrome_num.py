"""
Given an integer x, return true if x is a palindrome, and false otherwise.
e.g: 121 = True, -121 = Fasle, 10 = False
"""

def isPalindrome(num: int):
    if (num < 0):
        return False

    if num >=0 and num < 10:
        return True

    if num % 10 == 0 and num != 0:
        return False
        
    reversed_num = 0
    original = num

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original == reversed_num

if __name__ == "__main__":
    print(isPalindrome(121))
    print("\n")
    print(isPalindrome(-121))
    print("\n")
    print(isPalindrome(10))
    print("\n")
    print(isPalindrome(123321))
