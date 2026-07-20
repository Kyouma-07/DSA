class LC1011:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        n= len(weights)

        #possible range of answers
        min_weight = max(weights)
        max_weight = sum(weights)

        while (min_weight <= max_weight):
             mid = (min_weight + max_weight) // 2
             total_day = self.checkDays(weights, mid)

             if total_day <= days:
                max_weight = mid -1
             else:
                min_weight = mid + 1
        
        return min_weight
             
    
    def checkDays(self, weights : list[int], capacity: int):

            days = 1
            weighted_sum = 0

            for w in weights:
                if weighted_sum + w <= capacity:
                    weighted_sum += w
                else:
                    days += 1
                    weighted_sum = w

            return days