class LC540:

    def __init__(self):
        pass


    def singleNonDuplicate(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)- 1

        while (left < right):
             mid = (left+right)//2

             #keeping mid pointing to first element of the pair
             if mid % 2 == 1:
                mid -= 1
             
             #checking if pair is intact
             if nums[mid] == nums[mid +1]:
                #directly jumping to next pair
                left = mid + 2
             
             #if pair broken
             else:
                right = mid

        return nums[left]
