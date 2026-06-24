class LC35:

    def __init__(self):
        pass

    def searchInsert(self, nums: list[int], target: int) -> int:
      return __import__("bisect").bisect_left(nums, target)
    
    def searchInsert1(self, nums: list[int], target: int) -> int:
      n = len(nums)
      left, right = 0 , n-1
      ans = n

      while(left <= right):
         mid = (left+right)//2

         if nums[mid] >= target:
            ans = mid
            right = mid -1

         else:
          left = mid +1
        
      return ans 