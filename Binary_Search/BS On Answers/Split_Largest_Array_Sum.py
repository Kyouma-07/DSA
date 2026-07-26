class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        

        #dont split 
        #ask - "Can I split the array into at most k subarrays such that every subarray has sum ≤ X?"

        #minmum max val can be the max(nums), max val cannot be lower than this.
        left = max(nums)
        right = sum(nums)
        ans = -1

        n = len(nums)   # total elements in the array

        #edge case :- if the "subarray" > "total elements" , the split is impossible
        if k > n:
            return -1
        
        while( left <= right):
             mid = (left + right) //2

             if self.checkSplit( nums, mid, k):
                ans = mid
                right = mid - 1
             else:
                left = mid + 1
        
        return ans

    def checkSplit(self, nums: list[int], limit : int , k: int) -> bool:
        subarray = 1
        total_sum = 0

        for num in nums:
            if total_sum + num > limit:
                subarray += 1
                total_sum = num
            else:
                total_sum += num
        
        return subarray <= k

