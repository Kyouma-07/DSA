class LC15:

    def __init__(self):
        pass

    def threeSum(self, arr: list[int]) -> list[list[int]]:

        n= len(arr)
        res = set()

        for i  in range(n):
            for j in range(i+1 , n):
                for k in range(j+1, n):

                    if(arr[i] + arr[j] + arr[k] == 0):
                        res.add(tuple(sorted((arr[i], arr[j], arr[k]))))
        

        return [list(t) for t in res]


    def threeSum2(self, arr : list[int]) -> list[list[int]]:

        n = len(arr)
        res= set()
        freq = {}

        for i in range(n):
            for j in range(i+1,n):
                num = -(arr[i] + arr[j])

                if num in freq:
                    res.add(tuple(sorted((arr[i], arr[j], num))))
                else:
                    freq[arr[j]] = 1
            
            freq.clear()
        
        return [list(t) for t in res]


    def threesum3(self, arr: list[int]) -> list[list[int]]:

        n= len(arr)
        arr.sort()
        res = []

        for i in range(n):

            #skip all the duplicates
            if i > 0  and arr[i] == arr[i-1]:
                continue

            left, right = i + 1,  n-1

            while left < right:
                val = arr[i] + arr[left] + arr[right]

                if val == 0:
                    res.append([arr[i], arr[right], arr[left]])

                    #skipping duplicates from left
                    while left < right  and arr[left] == arr[left+1]:
                        left += 1
                    
                    #skipping duplicates from right
                    while left <right  and arr[right] == arr[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif val < 0:
                    left += 1
                else:
                    right -= 1
            
        
        return res

