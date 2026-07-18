class LC1482:


    def __init__(self):
        pass


    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        
        n = len(bloomDay)  #total_flowers

        #check if its possible to make  the bouquet
        if m * k > n:
            return -1
        
        #earliest day / last_day
        min_day = min(bloomDay)
        max_day = max(bloomDay)
        answer = -1


        while (min_day <= max_day):
            mid_day = (min_day + max_day) //2
            
            #can we make boquet in this day
            if self.canMake(bloomDay, mid_day , m , k):
                answer = mid_day  # valid day
                max_day = mid_day - 1
            else:
                min_day = mid_day +1

    
        return  answer


    def canMake(self, bloomDay: list[int], day : int, m : int , k: int) -> bool:

        flower = 0
        boquet = 0

        #checking for every flower
        for bloom in bloomDay:
            #if this flower has been bloomed by that day
            if bloom <= day:
                 flower += 1

                 #check if the 'flowers' already make 1 boquet
                 if flower == k:
                     boquet += 1
                     flower = 0 # reset flower to 0 , same flower cannot be used again
            else:
                flower = 0   # flower hasn't bloomed , adjacency breaks
        
        #returning true is we made enough boquets.
        return  boquet >= m
    