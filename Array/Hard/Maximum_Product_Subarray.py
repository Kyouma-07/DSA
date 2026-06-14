class LC152:

    def __init__(self):
        pass


    def maxProduct(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        #brute:
        max_prod = 0
        for i in range(len(nums)):
            current_prod = 1
            for j in range(i, len(nums)):
                current_prod *= nums[j]

                if current_prod > max_prod:
                    max_prod = max(max_prod, current_prod)
        
        return max_prod


    def maxProduct1(self, arr: list[int]) -> int:

        pre = 1
        suff= 1
        ans = float('-inf')
        n = len(arr)

        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            
            pre *= arr[i]
            suff *= arr[n-i-1]

            ans = max(ans, pre, suff)
        
        return int(ans) 
    
    def maxProduct2(self, nums: list[int]):
        max_prod = min_prod = ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])

            ans = max(ans, max_prod)

        return ans