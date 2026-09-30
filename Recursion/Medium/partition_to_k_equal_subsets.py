class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        if max(nums) > target:
            return False
        
        nums.sort(reverse=True)

        buckets = [0] * k

        def backtrack(index):
            
            if index == len(nums):
                return True

            num = nums[index]

            for i in range(k):
                
                #bucket overflow: early pruning:
                if buckets[i] + num > target:
                    continue

                #if putting in adjacent bucket provides the same sum , no need to explore cause same sum:
                if i > 0 and buckets[i] == buckets[i - 1]:
                    continue

                #add the sum to the bucket: choose
                buckets[i] += num
                
                #undo:
                if backtrack(index + 1):
                    return True
                
                #explore:
                buckets[i] -= num

            return False

        return backtrack(0)

#time : for each element , we can put them in K buckets , so k^n
#space : recursion depth = n elements = 0(n) , array bucket = K , 0(n+k)