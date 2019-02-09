"""
Question: Find the only duplicate element in a sorted array. Numbers range from 0 to n-2
example: Array [0,1,2,3,4,5,5,6,7]
Answer:5
"""

"""
The first solution: linear search
"""
def find_duplicate(array):
    n = len(array)
    for i in range(n-1):
        if array[i+1] == array[i]:
            return i
# Time complexity is O(n), space complexity is O(1)
            
"""
The second solution: math calculation; first find the sum of array sum, find the expected
value of array if it has no duplicates expected, then the duplicate number should
be len(array)-1-(expected - sum)
"""
def find_duplicate(array):
    n = len(array)
    expected = n*(n-1)/2
    return int(n-1-(expected - sum(array)))

# Time complexity is O(n), space complexity is O(1)
    
"""
The third solution: take advantage of the fact that the array is sorted, use binary
search to achive the fastest speed. The problem is to try find the first value that 
is smaller than the index. If array[mid] == mid, then low should be adjusted; if
array[mid] < mid, then high should be adjusted; when break out of loop, we find the 
duplicate value
"""
def find_duplicate(array):
    n = len(array)
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if array[mid] == mid:
            low = mid + 1
        elif array[mid] < mid:
            high = mid - 1
        
    return array[mid]

# Time complexity is O(log(n)), space complexity is O(1)
        
    
    
    
    
    
array = [0,1,2,3,4,5,5,6,7]
print(find_duplicate(array))

array = [0,1,2,3,4,5,6,7,7]
print(find_duplicate(array))

array = [0,1,1,2,3,4,5,6,7]
print(find_duplicate(array))