class LC875:

     def __init__ (self):
          
          pass   
     def minEatingSpeed(self, piles: list[int], h: int) -> int:
                left = 1
                right = max(piles)

                while (left <= right):
                    mid = (left +right) //2
                    total_hours = self.speed( piles, mid)

                    if total_hours <= h:
                        right = mid - 1
                    else:
                        left = mid  + 1
                
                return left


     def speed (self , piles: list[int], num : int):
                time = 0
                for bananas in piles:
                    time += (bananas + num - 1) // num
                
                return time