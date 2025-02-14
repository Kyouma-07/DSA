"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


"""



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        check1 = str(x)  
        if check1 == "".join(reversed(check1)):  
            return True
        else:
            return False  
        
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        check1 = x
        sum = 0
        while( check1 != 0 ):
            temp = check1%10
            sum = sum*10 + temp
            check1 = check1//10

        if(sum == x  ):
            return True
        else:
             return False