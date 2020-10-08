"""
Given an array containing N integers, and a value K, Print the sum of all subarrays of length K within array.
For example,
if the array is [1, 2, 3, 4, 5] and K = 3. Then print the sum of all subarrays containing 3 elements starting from the very first subarray.

The first subarray in this case, will be [1, 2,3] having a sum of 6.
Second subarray will be [2, 3, 4] having a sum of 9.
Third subarray will be [3, 4, 5] having a sum of 12.
nput
Each input file starts with t, which is the total number of test cases. Each test case consists of two lines :

First line of each test case consists of N and K , where N is the number of elements in the array and K is the size of subarray.
Second line consists of N space separated integers which are the contents of the array.
Output
For each test case output the sum of each subarray in a different line as shown below

Example
Input:
2
5 3
1 2 3 4 5
4 2
2 3 4 1

Output:
6
9
12
5
7
5

Constraints
3 <= N <= 10^6
3 <= K <= N
"""

def getksubarraySum(arr, k):
    sum, n, output = 0, len(arr), []
    for i in range(min(n, k)):
        sum += arr[i]

    output.append(sum)
    if k >= n:
        return output

    for i in range(k, n):
        sum = sum - arr[i - k] + arr[i]
        output.append(sum)
    return output


t = int(input())
for _ in range(t):
    inp = [int(j) for j in input().split()]
    arr = []
    arr = [int(k) for k in input().split()]
    result = getksubarraySum(arr,inp[1])
    for num in result:
        print(num)



