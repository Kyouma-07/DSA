import math

class LC744:

    def _init__(self):
        pass


    def minmaxGasDist(self, stations: list[int], k: int) -> float:

        left = 0
        #safe upperbound
        right = stations[-1] - stations[0]

        #tight upperbound: since the answer can never exceed the largest existing gap.
        """
        right = max(
    stations[i + 1] - stations[i]
    for i in range(len(stations) - 1)
)
        """

        while right - left > 1e-6:

            mid = (left + right) /2  #can be a floating val

            if self.checkDistance(stations,mid, k):
                right = mid
            else:
                left = mid

        return right

    def checkDistance(self, stations: list[int], distance: float , k: int) -> bool:

        station_needed = 0

        for i in range( 0 ,len(stations)-1):
            gap = stations[i+1] - stations[i]
            station_needed += math.ceil(gap/distance) - 1

        return station_needed <= k




