"""
Given two binary strings a and b, return their sum as a binary string. 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

def addBinary_ver2(a: str, b: str) -> str:
    carry = 0
    res = []

    c_a, c_b = len(a) - 1, len(b) -1

    while c_a >=0 or c_b >= 0 or carry:
         if c_a >= 0:
            carry += int(a[c_a])
            c_a -= 1
         if c_b >= 0:
            carry += int(b[c_b])
            c_b -= 1

         res.append(str(carry % 2))
         carry //= 2

    return ''.join(res[::-1])
            
     
def addBinary_ver1(a, b):
    a_list = [item for item in map(int, a)]
    b_list = [item for item in map(int, b)]
    result = []
    a_counter = len(a_list) - 1
    b_counter = len(b_list) - 1
    carry = 0

    while a_counter >= 0 or b_counter >= 0:
        a = a_list[a_counter] if a_counter >= 0 else 0
        b = b_list[b_counter] if b_counter >= 0 else 0
        temp = a + b + carry
        if temp == 3:
                result.insert(0, 1)
                carry = 1
        elif temp == 2:
            result.insert(0, 0)
            carry = 1
        else:
            result.insert(0, temp)
            carry = 0

        a_counter -= 1
        b_counter -= 1

    if carry == 1:
        result.insert(0, 1)

    return "".join(item for item in map(str, result))

if __name__ == "__main__":
    print(addBinary_ver1("11", "1"))  # Output: "100"
    print(addBinary_ver2("11", "1"))  # Output: "100"
    print("----" * 15)
    print(addBinary_ver1("1010", "1011"))  # Output: "10101"
    print(addBinary_ver2("1010", "1011"))  # Output: "10101"
    print("----" * 15)
    print(addBinary_ver1("1111", "1111"))  # Output: "11110"
    print(addBinary_ver2("1111", "1111"))  # Output: "11110"