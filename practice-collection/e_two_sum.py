"""
Two sum problem.
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Make hashmap key as nums array value and its value as nums array index
    hashmap = {} 
    for index, num in enumerate(nums):
        print(f"Iteration {index} : searching for {target - num} in {hashmap}")
        if (target - num) in hashmap: # this by default searches in keys
            return[index, hashmap[target-num]]
        hashmap[num] = index
    return hashmap

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
    print("\n")
    print(twoSum([3,2,4],6))
    print("\n")
    print(twoSum([3,3],6))