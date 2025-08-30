"""
You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .
Example
 
There are  and  at indices  and . Return .
Function Description
Complete the countTriplets function in the editor below.
countTriplets has the following parameter(s):
int arr[n]: an array of integers
int r: the common ratio
Returns
int: the number of triplets
Input Format
The first line contains two space-separated integers  and , the size of  and the common ratio.
The next line contains  space-seperated integers .
Constraints

Sample Input 0
4 2
1 2 2 4
Sample Output 0
2
Explanation 0
There are 2 triplets in satisfying our criteria, whose indices are (0,1,3) and (0,2,3)

Sample Input 1
6 3
1 3 9 9 27 81
Sample Output 1
6
Explanation 1
The triplets satisfying are index (0,1,2),(0,1,3) ,(1,2,4) ,(1,3,4) ,(2,4,5)  and (3,4,5).

Sample Input 2
5 5
1 5 5 25 125
Sample Output 2
4
Explanation 2
The triplets satisfying are index (0,1,3),(0,2,3) ,(1,3,4) ,(2,3,4) .
"""
def countTriplets(arr, r):
    left_count = {}
    right_count = {}
    res = 0
    for i in range(len(arr)):
        right_count[arr[i]] = right_count.get(arr[i], 0) + 1

    for i in range(len(arr)):
        curr = arr[i]        
        right_count[curr] -= 1
        
        if curr % r == 0 and curr//r in left_count and (curr * r) in right_count:
            res += left_count[curr/r] * right_count[curr * r]
        left_count[curr] = left_count.get(curr, 0) + 1
        
    return res

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)