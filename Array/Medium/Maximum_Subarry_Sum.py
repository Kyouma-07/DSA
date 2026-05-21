class LC53:

    def __init__ (self):
        pass

    
    #Brute Time = O(n^2)
    def maxSubArray(self, arr : list[int]):

        max_sum = float('-inf')
        start = 0
        end = 0

        for i in range (len(arr)):
            current_sum = 0

            for j in range (i , len(arr)):
                current_sum += arr[j]

                if current_sum > max_sum :
                    max_sum = current_sum
                    start = i
                    end = j 


        return max_sum, end- start +1, arr[start:end+1]

    #Kadane's Algorithm  Time = O(n) 
    def maxSubArray1(self, arr: list[int]):
        max_sum = float('-inf')
        start = 0
        end = 0
        temp_start = 0
        current_sum = 0

        for i in range (len(arr)):
            current_sum += arr[i]

            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start
                end = i
            
            if current_sum < 0:
                current_sum = 0
                temp_start = i +1
        
        return max_sum , end - start +1 , arr[start : end +1]
    
    #kadane's algo using formulae:
    def maxSubArray2(self, nums: list[int]) -> int:
        curr = ans = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)
            ans = max(ans, curr)
        return ans

if __name__ == "__main__":
    print("Hello world!!")
    obj = LC53()
    print(obj.maxSubArray1([-2,1,-3,4,-1,2,1,-5,4]))