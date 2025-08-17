"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

def maxArea(height):
    max_capacity = 0
    
    i = 0
    j = len(height) - 1

    while i < j:
        w = j - i
        h = height[i] if (height[i] < height[j]) else height[j]
        if max_capacity < (w * h):
            max_capacity = w * h

        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1

    return(max_capacity)

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))
    print(maxArea([1,1]))