class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:

        left = 1
        right = 10**7
        ans = -1

        #there is no chance of making it, regardless of speed.
        if hour <= len(dist) - 1:
          return -1

        while (left <= right):

            mid = (left + right)//2
            
            if self.checkSpeed(dist, mid , hour):
                ans = mid
                right = mid - 1
            else:
                left = mid +1
        
        return ans
    

    def checkSpeed(self, dist: list[int], speed: int, hour : float) -> bool:

        time = 0
        
        for i  in range(0 , len(dist) -1):
            time += (dist[i] + speed - 1) //speed
        
        time += dist[-1] / speed

        return time <= hour

            