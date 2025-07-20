"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    prefix = strs[0]
    prefix_len = len(prefix)

    for s in strs[1:]:
        while prefix != s[0:prefix_len]:
            prefix_len -= 1
            if prefix_len == 0:
                return ""
            prefix = prefix[0:prefix_len]

    return prefix

if __name__ == "__main__":
    print(longestCommonPrefix(["dog", "racecar", "car"]))
    print(longestCommonPrefix(["flower", "flow", "flight"]))