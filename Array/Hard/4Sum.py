class LC18:

    def __init__(self):
        pass


    def fourSum(self, arr: list[int], target:  int) -> list[list[int]]:

        n = len(arr)
        res = []

        for i in range(n):
            for j in range(i+1 , n):
                seen = set()

                for k in range(j+1, n):
                    fourth = target -( arr[i] + arr[j] + arr[k])

                    if fourth in seen:
                        quad = tuple(sorted([arr[i], arr[j], arr[k], fourth]))
                        res.append(quad)
                    
                    seen.add(arr[k])
            
        return [list(q) for q in res]


    def fourSum2(self, arr: list[int], target: int) -> list[list[int]]:
        n = len(arr)
        arr.sort()
        res = []

        for i in range(n):
            if i > 0  and arr[i] == arr[i-1]:
                    continue
            for j in range(i+1, n):
                if j > i+1  and arr[j] == arr[j-1]:
                    continue
                
                
                left, right = j+1 , n-1

                while left < right:
                    val = arr[i] + arr[j] + arr[left] + arr[right]

                    if val == target:
                         res.append([arr[i], arr[j], arr[left], arr[right]])

                         while left < right and arr[left] == arr[left+1]:
                             left += 1
                        
                         while left < right and arr[right] == arr[right-1]:
                             right -= 1
                         
                         left += 1
                         right -= 1

                    elif val < target :
                        left += 1
                    else:
                        right -= 1
            
        return res

