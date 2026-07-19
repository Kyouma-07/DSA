class LC1283:

    def __init__(self):
        pass
    

    def smallestDivisor(self, arr: list[int], threshold: int) -> int:
        
        left = 1
        right = max(arr)

        while (left <= right):
            mid = (left + right) //2

            total_sum = self.checkSum(arr, mid)

            if total_sum <= threshold:
                right = mid - 1
            else:
                left = mid +1
        
        return left
    

    def checkSum(self, arr : list[int], num : int):
        total = 0 

        for i in arr:
            total += (i + num - 1) // num
        
        return total