"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

"""

class Solution:
    def reverse(self, x: int) -> int:

        sum = 0
        if x < 0 :
            sum = int (str(x)[1:][::-1]) *-1
        else:
            sum = int( str (x)[::-1])
        
        if sum > 2**31-1 or sum < -2 **31:
            return 0
        
        return sum