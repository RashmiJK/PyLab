"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""
def expand_around_centre(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longestPalindrome(s):
    if not s:
        return ""
    
    start = end = 0

    for i in range(len(s)):
        odd_len = expand_around_centre(s, i, i)
        even_len = expand_around_centre(s, i, i+1)
        max_len = max(odd_len, even_len)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start:end+1]

if __name__ == "__main__":
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))