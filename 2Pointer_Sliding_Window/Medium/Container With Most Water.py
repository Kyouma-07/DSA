class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        n = len(height)

        left = 0
        right = n-1

        while (left < right):
            area = 0
            if height[left] > height[right]:
                width = right - left
                area = width * height[right]  #use shorter height for area.. otherwise wateroverflow
                right -= 1
            else:
                width = right - left
                area = width * height[left]
                left += 1

            max_area = max(max_area, area)
        
        return max_area