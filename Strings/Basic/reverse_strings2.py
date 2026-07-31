from typing import List
class Solution:
    def reverseStr1(self, s: str, k: int) -> str:
        
        char = list(s)

        #jump every 2*k block
        for i in range(0 , len(s)- 1, 2*k):
            left = i 
            #check for condition  ( <2k or <k)
            right = min(i + k - 1, len(s) - 1)


            #swap till necessary
            while(left < right):
                char[left], char[right] = char[right], char[left]
                left += 1
                right -= 1
            
        return "".join(s)



    def reverseStr2(self, s: str, k: int) -> str:
        
        char = list(s)
        
        start = 0
        n = len(s)

        while start < n:
            remaining = n - start

            if remaining >= k:
                left = start
                right = start + k - 1

            else:
                left = start
                right = n - 1

            while left < right:
                char[left], char[right] = char[right], char[left]
                left += 1
                right -= 1

            start += 2 * k

        return "".join(char)


