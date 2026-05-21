class LC121:

    def __init__(self):
        pass

    def maxProfit(self, arr: list[int]) -> int:

        min_val = arr[0]
        max_profit = 0
        profit = 0

        for i in range(len(arr)):
            min_val = min( min_val ,  arr[i])
            profit = arr[i] - min_val
            max_profit = max(max_profit, profit)
        
        #cal profit first, and then update min , max_profit at last , this is more accurate logically.
        return max_profit
    

    #using kadane's algo (calculate the max subarray with max_profit (subarray here is difference in price of stocks))
    # [7,1,5, 3, 6, 4] = [ -6,4,-2,3,-2]
    def maxProfit1(self, arr: list[int]) -> int:

        curr_profit = 0
        max_profit = 0

        for i in range (1 , len(arr)):
            diff = arr[i] - arr[i-1]

            curr_profit += diff

            if curr_profit > max_profit:
                max_profit = curr_profit
            
            if curr_profit < 0:
                curr_profit = 0
        
        return max_profit
