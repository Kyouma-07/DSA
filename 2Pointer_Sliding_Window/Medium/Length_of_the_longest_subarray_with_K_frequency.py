class LC2958:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        
        freq = {}
        n = len(nums)
        left = 0
        ans = 0

        for right in range(n):
            freq[nums[right]]  = freq.get(nums[right], 0) + 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            
            ans = max(ans , right - left +1)
        
        return ans
                