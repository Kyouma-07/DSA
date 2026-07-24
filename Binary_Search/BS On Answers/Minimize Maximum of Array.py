class LC2439:
     
     def __init__(self):
          pass

     #brute
     #O(n^2)
     def minimizeArrayValue1(self, nums: list[int]) -> int:
        
        changed = True

        while changed:
            changed = False

            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    changed = True

                    diff = nums[i] - nums[i - 1]

                    # Move half the difference (rounded up), instead of single pass
                    move = (diff + 1) // 2

                    nums[i] -= move
                    nums[i - 1] += move

        return max(nums)

     #optimal:
     #O(log(max) * n)
     def minimizeArrayValue2(self, nums: list[int]) -> int:
        
        #ask :- "Is it possible to make every element <=X "
        #search space  1 to max(arr)

        n= len(nums)
        left = 0
        right = max(nums)
        ans = max(nums)

        while(left <= right):

            #possible answer:
            mid = (left + right) //2

            if self.check(nums,mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
    
     def check(self, nums: list[int], value : int) -> bool:

        capacity = 0 

        for num in nums:
            if num <= value:
                capacity += ( value - num )
            else:
                overflow = num - value

                if overflow > capacity:
                    return False
                
                capacity -= overflow
        
        return True


    #best:
    #o(n)
     def minimizeArrayValue3(self, nums: list[int]) -> int:
        
        #using prefix-sum:
        ans = 0
        prefix_sum = 0
        for i , num in enumerate(nums):
            prefix_sum += num

            needed = (prefix_sum + i ) // (i+1)
            ans = max(ans , needed)
        

        return ans