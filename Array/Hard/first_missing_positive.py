class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        #key obervation :- > the missing 1st positive no. will be in the range of 1 to n +1
        #max_possible ans, n = [ 1, 2, 3, 4, 5], missing positive = n+1 = 6
        #n = [ 2, 3, 4, 5, 6] , missing +ve = 1
        #=> missing +ve can never be more than n+1 

        #range = 1 to  n+1 (skip the rest)
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                crr_idx = nums[i] - 1
                #swap
                nums[i], nums[crr_idx] = nums[crr_idx], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1