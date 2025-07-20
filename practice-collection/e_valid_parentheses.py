"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Example 5:
    Input: s = "([)]"
    Output: false

Notes:
    1. if not stack => Enter, if stack is empty
    2. or => first factor satisfied, skip the second after or

"""

def isValidParenthesis(s: str) -> bool :
    stack = []
    mapping = {
        ")" : "(",
        "]":"[",
        "}" : "{"
    }

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack:
                return False
            elif mapping[char] != stack.pop():
                return False
            
    if stack:
        return False
    else:
        return True

def isValidParenthesisConcise(s: str) -> bool :
    stack = []
    mapping = {
        ")" : "(",
        "]":"[",
        "}" : "{"
    }

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False

    return not stack

def isValidParenthesisAnotherTechnique(s: str) -> bool :
    stack = []

    for i in range(len(s)):
        if stack:
            last = stack[-1]
            if is_pair(last, s[i]):
                stack.pop()
                continue
        stack.append(s[i])
    return not stack

def is_pair(last, cur):
    if last == "(" and cur == ")" or last == "{" and cur == "}" or last == "[" and cur == "]":
        return True
    return False


if __name__ == "__main__":
    print(isValidParenthesis("([])"))
    print(isValidParenthesisConcise("([])"))
    print(isValidParenthesisAnotherTechnique("([])"))