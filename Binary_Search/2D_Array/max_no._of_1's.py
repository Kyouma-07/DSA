class Maximum1:

    def __init__(self):
        pass

    def maximumOnes(self, arr: list[list[int]]) -> int:

        n = len(arr)
        ans = -1

        if len(arr) == 0:
            return -1

        max_count = 0

        for i in range( 0 , len(arr)):
            low_idx = __import__("bisect").bisect_left(arr[i],1)
            count = len(arr[i]) - low_idx

            if count > max_count: 
                max_count = count
                ans = i #return the row idx

        return ans