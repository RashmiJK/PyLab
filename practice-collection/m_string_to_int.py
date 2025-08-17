"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
"""
def myAtoi_ver2(s):
    s = s.strip()
    if not s:
        return(0)
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    num_list = []
    for ch in s:
        if ch >='0' and ch <= '9':
            num_list.append(str(ch))
        else:
            break
    num_str = "".join(num_list)

    if num_str:
        num = int("".join(num_list)) * sign
    else:
        num = 0

    if num < -2 ** 31:
        num = -2 ** 31
    elif num > 2 ** 31 - 1:
        num = 2 ** 31 - 1
    return num

def myAtoi_ver1(s):
    # Skip leading whitespaces
    # Handle optional sign
    # Read and convert digit (*10)
    # Apply sign and return
    if not s:
        return 0
    
    INT_MAX = 2**31 -1
    INT_MIN = -2**31

    i = 0
    n = len(s)

    while i < n and s[i] == ' ':
        i += 1

    if i == n:
        return 0
    
    sign = 1
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1

    res = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        res = res * 10 + digit

        if sign * res <= INT_MIN:
            return INT_MIN
        if sign * res >= INT_MAX:
            return INT_MAX
        
        i += 1

    return res * sign

if __name__ == "__main__":
    print(myAtoi_ver1("42"))
    print(myAtoi_ver2("42"))
    print("---"*10)

    print(myAtoi_ver1(". -042"))
    print(myAtoi_ver2(". -042"))
    print("---"*10)

    print(myAtoi_ver1("1337c0d3"))
    print(myAtoi_ver2("1337c0d3"))
    print("---"*10)

    print(myAtoi_ver1("0-1"))
    print(myAtoi_ver2("0-1"))
    print("---"*10)

    print(myAtoi_ver1("words and 987"))
    print(myAtoi_ver2("words and 987"))