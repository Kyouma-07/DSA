class LC229:

    def __init_(self):
        pass

    def majorityElement(self, arr: list[int]) -> list[int]:

        freq ={}

        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        

        
        res = []
        for key, value in freq.items():
            if value > len(arr)//3:
                res.append(key)
               
        return res


    def majorityElement1(self, arr: list[int]) -> list[int]:

        if not arr:
            return[]
        
        count1 = count2 = 0
        candidate1 = candidate2 = None

        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num , 1
            elif count2 == 0:
                candidate2, count2 = num , 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        for candidate in [candidate1, candidate2]:
            if candidate  is not None and arr.count(candidate) > len(arr)//3:
                res.append(candidate)
        
        return res