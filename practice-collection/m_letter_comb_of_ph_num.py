"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters. 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
# Backtracking is the best solution as it has significantly better space complexity
def letterCombinations_ver1(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def backtrack(idx, comb):
        if idx == len(digits):
            res.append(comb[:])
            return
        
        for letter in digit_to_letters[digits[idx]]:
            backtrack(idx + 1, comb + letter)

    res = []
    backtrack(0, "")

    return res

def letterCombinations_ver2(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    num_to_letters = {
        "1" : "",
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }
        
    if not digits:
        return []

    combinations = [letter for letter in num_to_letters[digits[0]]]
    if len(digits) == 1:
        return combinations

    index = 1
                
    while index < len(digits):
        temp_array = [letter for letter in num_to_letters[digits[index]]]
        result = []
        for char_l in combinations:
            for char_r in temp_array:
                result.append(char_l + char_r)
        index += 1
        combinations = result
    return(result)

if __name__ == "__main__":
    print(letterCombinations_ver1("234"))
    print(letterCombinations_ver2("23"))
    print("---"*10)
    
    print(letterCombinations_ver1(""))
    print(letterCombinations_ver2(""))
    print("---"*10)

    print(letterCombinations_ver1("2"))
    print(letterCombinations_ver2("2"))

