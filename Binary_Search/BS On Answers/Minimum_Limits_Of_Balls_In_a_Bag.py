class LC1760:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        
        #key idea => "can I make every bag have atleast X balls"
        #what to do = > " minimize the size of the largest bag"
        #note: whether a particular maximum bag size is achievable.

        #note: Across all bags combined, you can perform at most maxOperations splits. (not for each bag)
        
        #Possible ranges of answer:
        left = 1
        right = max(nums)
        ans = 0

        while (left <= right):
            mid = (left + right) // 2

            if self.canSplit(nums, mid, maxOperations):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
    

    def canSplit(self, nums: list[int], num: int, maxOperations: int) -> bool:

        n = len(nums)
        totalOperations = 0

        #totalOperations = Total Split - 1
        #ex => for  bag = 10 , x = 3 , we need 4 bags (3 + 3 +3 +1) , => total operations = 3

        for bags in nums:
            totalOperations += (bags - 1) // num

            if totalOperations > maxOperations:
                return False
        
        return True