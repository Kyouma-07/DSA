class Solution:
    def search(self, nums: list[int], target: int) -> int:

        return self.binarySearch(nums,0 , len(nums)-1, target)
        
    

    def binarySearch(self, nums:  list[int], low: int, high: int, target: int):

        if low > high:
            return -1
        
        mid = (low+high)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums,low , mid-1, target)
        else:
            return self.binarySearch(nums,mid+1, high,target)
        