class LC442:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # curr_arr = [4,5,2,7,8,2,3,1]
        # idx = [0,1,2,3,4,5,6,7]
        # correct_arr = [1,2,3,4,5,6,7,8]

        for i in range(n):
            while 0 < nums[i] <= n  and ( nums[i] != nums[nums[i] - 1] ):
                crr_idx = nums[i] - 1
                #swap
                nums[crr_idx], nums[i] = nums[i], nums[crr_idx]
        
        ans = []
        for i in range(n):
            if nums[i] != i+1:
                ans.append(nums[i])
        
        return ans
            