import math

class LC2594:
    
    def repairCars(self, ranks: list[int], cars: int) -> int:
        
        #range of possible time
        left = 1
        right = min(ranks) * (cars*cars)

        while( left  <=  right):

            mid = (left+ right) //2 #possible value of time

            if self.checkRepair(ranks, mid , cars):
                right = mid -1
            else:
                left = mid + 1
        
        return left
    

    def checkRepair(self, ranks : list[int], time : int , cars: int) -> bool:
        
        #no. of cars repaired
        repaired = 0

        #for each mech, how many cars they repair in "time" time
        for mechs in ranks:
            repaired += math.isqrt( time // mechs)

            # if the no. of cars reapired in "time" time >= cars that needs to be repaired, we get the required time and return true
            if repaired >= cars:
                return True
        
        return False


#ask : "If I am given T minutes, is it possible to repair at least "n" cars?"
#note: - the mechs works simultaneously => their time doesnt need to add up , time = time required by max(ranks)