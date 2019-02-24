"""
443. String Compression
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
"""

"""
Solution:
"""
def compress(chars):
    count = 1 # Intialize count to be 1
    i = 1 # starting index to be 1
    l = len(chars) # length of chars
    index = -1
    while i < l:
        if chars[i] == chars[i-1]: # when two sbsequent letters are the same
            count += 1 # count plus 1
        else:
            index += 1 # find the index to write
            chars[index] = chars[i-1] # first write the character
            if count > 1: # when count is larger than 1, we write the count
                new_count = str(count) # 12 need to be wrote as '1','2'
                for letter in new_count:
                    index += 1
                    chars[index] = letter  
            count = 1 # reset count to be 1
        i += 1 
    index += 1 # when iterate over, need to add the last character
    chars[index] = chars[i-1]
    if count > 1:
        new_count = str(count)
        for letter in new_count:
            index += 1
            chars[index] = letter
    return index+1 # the length of the character

# Time complexity: O(n), space complexity: O(1)