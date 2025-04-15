# Time complexity and Big-O Notation

Time complexity describes how the execution time of an algorithm grows relative to the input size. We use Big-O notation to express this relationship mathematically.

Below are the most common time complexities.

## O(1) - Constant time
Operations that take the same amount of time regardless of input size.

## O(log n) - Logarithmic time

A logarithm answers the question "How many times do I need to multiply a base number by itself to get the target number?"

| Power of 2 (just for reference) | Log₂ |
|------------|------|
| 2¹ = 2     | 1    |
| 2² = 4     | 2    |
| 2³ = 8     | 3    |
| 2⁴ = 16    | 4    |
| 2⁵ = 32    | 5    |
| 2⁶ = 64    | 6    |
| 2⁷ = 128   | 7    |

Notice how the input grows exponentially (2, 4, 8, 16...), but the logarithm value (the result) grows linearly (1, 2, 3, 4...).
![Logarithmic Time Complexity](images/log_time_complexity.png)

* The curve rises quickly for small input sizes but dramatically flattens as input size increases
* If your input size doubles, your algorithm only needs one additional operation.
* For a binary search on an array:  
    10 elements ≈ log₂(10) ≈ 3.32 steps (max)  
    1,000 elements ≈ log₂(1000) ≈ 10 steps (max)  
    1,000,000 elements ≈ log₂(1,000,000) ≈ 20 steps (max)  
    O(log n) Is Efficient.  
This is why search algorithms like binary search, balanced binary search trees - they scale exceptionally well as data size increases.

## O(n) - Linear time
Operations that process each element in the input exactly once. The execution time grows linearly with the input size. It examines each element exactly once, regardless of the array's content or order.

## O(n log n) - Linearithmic Time
This complexity often appears in efficient sorting algorithms like Merge Sort, Quick Sort, and Heap Sort. Linearithmic time complexity combines linear and logarithmic growth rates. 


## O(n<sup>2</sup>) - Quadratic Time
Operations that involve nested iterations over the input. Example bubble sort.

## O(2<sup>N</sup>)

## O(N!)


# Summary
![](images/graph.png)