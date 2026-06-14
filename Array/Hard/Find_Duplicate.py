class LC287:

    def __init__(self):
        pass


    def findDuplicate(self, arr: list[int]) -> int:

        low = 1
        high = len(arr)

        while low < high:
            mid = (low + high)//2
            count  = 0

            for num in arr:
                if num < mid:
                    count += 1
            
            if count > mid:
                high = mid
            else:
                low = mid +1

        return low