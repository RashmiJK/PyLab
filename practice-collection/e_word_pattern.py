"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""

def wordPattern_v1(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    # O(n**2) => Time complexity beacuse of value in p_dict.values()
    words = s.split()
    if len(pattern) != len(words):
        return False

    p_dict = {}

    for i in range(len(pattern)):
        key = pattern[i]
        value = words[i]

        if key in p_dict:
            # key found
            if p_dict[key] != value:
                return False  
        elif value in p_dict.values(): 
            if key not in p_dict:
                return False              
        else:
            p_dict[pattern[i]] = words[i] 
    return True

def wordPattern_v2(pattern, s):
    # Two hash maps. time : O(n), space : O(n)
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
        
    return True

if __name__ == "__main__":
    print(wordPattern_v1("abba", "dog cat cat dog"))
    print(wordPattern_v2("abba", "dog cat cat dog"))

    print("---"*10)

    print(wordPattern_v1("abba", "dog cat cat fish"))
    print(wordPattern_v2("abba", "dog cat cat fish"))

    print("---"*10)

    print(wordPattern_v1("aaaa", "dog cat cat dog"))
    print(wordPattern_v2("aaaa", "dog cat cat dog"))