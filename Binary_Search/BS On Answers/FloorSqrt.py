class FloorSqrt:

    def __init__ (self):
        pass


    def findSqrt(self ,num: int) -> int:
        left = 0
        right = num

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= num:
                left = mid + 1
            else:
                right = mid - 1

        return right
