"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

"""
def reverse_ver2(x):
    result = 0
    if x < 0:
        result = int(str(x)[1:][::-1]) * -1
    else:
        result = int(str(x)[::-1])

    if result > (2 ** 31) - 1 or result < -2 ** 31:
        return(0)
    else:
        return(result)


def reverse_ver1(x):
    if not x:
        return(x)

    sign = 1
    if x < 0:
        sign = -1
        x = x * -1

    result = 0
    i = 0

    while x:
        rem = x % 10
        result = rem + result * (10 * i)

        x = x // 10
        i = 1
        
    result = result * sign

    if result > (2 ** 31) - 1 or result < -2 ** 31:
        return(0)
    else:
        return(result)

if __name__ == "__main__":
    print(reverse_ver1(123))
    print(reverse_ver2(123))
    print("---"*10)
    print(reverse_ver1(-123))
    print(reverse_ver2(-123))
    print("---"*10)
    print(reverse_ver1(120))
    print(reverse_ver2(120))
    #print(reverse('None'))