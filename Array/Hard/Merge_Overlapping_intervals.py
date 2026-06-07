class LC56:

    def __init__(self):
        pass

    def mergeBrute(self, arr: list[list[int]]) -> list[list[int]]:
        n= len(arr)
        arr.sort()
        res = []

        for i in range(n):
            start = arr[i][0]
            end = arr[i][1]
            if ( len(res) != 0 and end <= res[-1][1]):
                continue

            for j in range(i+1, n):
                if arr[j][0] < end:
                    end = max(end, arr[j][1])
                else:
                    break
            
            res.append([start,end])
        
        return res

    def mergeOptimal(self, arr: list[list[int]]) -> list[list[int]]:
        n= len(arr)
        arr.sort()
        res = []

        for i in range(n):
            if ( len(res) == 0 or  arr[i][0] > res[-1][0]):
                res.append(arr[i])  #current_interval
            
            res[-1][1] = max(res[-1][1] , arr[i][1])  #merge_intervals
        
        return res