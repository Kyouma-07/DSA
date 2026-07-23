class LC2517:
    def maximumTastiness(self, price: list[int], k: int) -> int:
         n = len(price)

         price.sort()  #sort for greedy check

         #range of possible tastiness values
         left = 1
         right = price[-1] - price[0]

         ans = 0
         
         while (left <= right):

            mid = (left + right) // 2

            if self.isTasty(price, mid , k):
                ans = mid

                #checking for maximum tastiness
                left = mid +1
            else:
                right = mid - 1

         return ans

    
    def isTasty (self, price : list[int], tastiness: int, candies: int) -> bool:

        #keeping 1st candy at first index
        lastPlacedCandy = price[0]
        placed  = 1

        for i in range ( 1, len(price)):
            if price[i] - lastPlacedCandy >= tastiness:
                placed += 1
                lastPlacedCandy = price[i]

                if placed == candies:
                    return True
        
        return False