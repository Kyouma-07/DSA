class LC448:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        #optimal
        #using cyclic sort:
        
        n = len(nums)

        # curr_arr = [ 4, 3, 2, 7, 8, 2, 3, 1]
        # indices = [0 , 1, 2, 3, 4, 5, 6, 7, ]
        # 1 to n = [ 1, 2, 3, 4, 5, 6, 7, 8]

        for i in range(n):

            #continue till we find either duplicates or till 1 < nums[i] <= n:
            while 0 < nums[i] <= n and  ( nums[i] !=  nums[ nums[i] - 1]):
                curr_idx = nums[i] - 1
                #swap
                nums[i], nums[curr_idx] = nums[curr_idx] , nums[i]
            
        ans = []
        for i in range(n):
            if nums[i]  != i + 1:
                ans.append(i +1 )
        
        return ans
            
        
    