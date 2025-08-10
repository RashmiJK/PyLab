"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

def plusOne_ver3(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] +1 < 10:
            digits[i] += 1
            return digits
        
        digits[i] = 0

        if i == 0:
            return [1] + digits

def plusOne_ver2(digits):
    d_counter = len(digits) - 1
    carry = 0
    increment = 1
    while d_counter >= 0:
        inter_sum = digits[d_counter] + increment + carry
        increment = 0  # Only the last digit needs to be incremented by 1
        if inter_sum >= 10:
            digits[d_counter] = inter_sum % 10
            carry = 1
        else:
            digits[d_counter] = inter_sum
            carry = 0   
            return digits     
        d_counter -= 1
    if carry == 1:
        digits.insert(0, 1)
    return digits

def plusOne_ver1(digits):
    num_str = str(int("".join(map(str, digits))) + 1)
    return [int(digit) for digit in num_str]

if __name__ == "__main__":
    print(plusOne_ver1([1,2,3]))
    print(plusOne_ver2([1,2,3]))
    print(plusOne_ver3([1,2,3]))
    print("----"*10)
    print(plusOne_ver1([4,3,2,1]))
    print(plusOne_ver2([4,3,2,1]))
    print(plusOne_ver3([4,3,2,1]))
    print("----"*10)
    print(plusOne_ver1([9]))
    print(plusOne_ver2([9]))
    print(plusOne_ver3([9]))
    print("----"*10)
    print(plusOne_ver1([9,9,9,9]))
    print(plusOne_ver2([9,9,9,9]))
    print(plusOne_ver3([9,9,9,9]))