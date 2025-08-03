"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
def lengthOfLastWordVer1(s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        s_list = s.strip().split()
        return len(s_list[-1])

def lengthOfLastWordVer2(s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        end = len(s) - 1

        while s[end] ==" ":
               end -= 1
        start = end
        while start >=0 and s[start]!= " ":
            start -= 1
        return end-start

if __name__ == "__main__":
    print(lengthOfLastWordVer1("Hello World"))
    print(lengthOfLastWordVer2("Hello World"))
    print("---" * 10)
    print(lengthOfLastWordVer1("   fly me   to   the moon  "))
    print(lengthOfLastWordVer2("   fly me   to   the moon  "))
    print("---" * 10)
    print(lengthOfLastWordVer1("luffy is still joyboy"))
    print(lengthOfLastWordVer2("luffy is still joyboy"))
