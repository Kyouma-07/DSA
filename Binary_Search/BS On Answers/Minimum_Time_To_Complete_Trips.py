class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
         n = len(time)

         left = 1

         #safer upperbound (max time alone cannot complete all the trips)
         right = min(time) * totalTrips

         while (left <= right):

            mid= (left + right) //2

            if self.checkTime(time, mid, totalTrips):
                right = mid -1
            else:
                left = mid +1
         
         return left
    

    def checkTime(self, time : list[int], value : int , totalTrips : int):
        completed = 0

        for num in time:
            completed += (value//num)
        
        #return True if completed  enough trips
        return completed >= totalTrips