class LC169:

    def __init__(self):
        pass

    def MajorityElement(self, arr: list[int]):

        hash = {}
 
        for i in arr:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        
        max_count = -1
        res = None
        
        for key, value in hash.items():
            if value > max_count:
                max_count = value
                res = key

        return res

    #Moore's Voting Algorithm
    def majorityElement(self, arr: list[int]):

        count = 0
        candidate = None

        # voting pahse ( this part of code is enough) finding candidate
        for i in arr :

            if count == 0:
                candidate = i
            
            if i == candidate:
                count += 1
            
            else:
                count -= 1
        
        #verification ( where maj_elem  freq > n/2)
        count = 0
        for i in arr:
            if i == candidate:
                count += 1
        
        if count >  len(arr)//2:
            return candidate
        else:
            return -1
