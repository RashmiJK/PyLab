"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

def findSubStrVer1(haystack: str, needle: str) -> int:
    return(haystack.find(needle))

def findSubStrVer2(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

if __name__ == "__main__":
    print(findSubStrVer1("sadbutsad", "sad"))
    print(findSubStrVer2("sadbutsad", "sad"))

    print("---" * 15)

    print(findSubStrVer1("leetcode", "leeto"))
    print(findSubStrVer2("leetcode", "leeto"))