class LC1552:
    def maxDistance(self, position: list[int], m: int) -> int:
        
        position.sort() #sorting to maintain the greddy approach of placing balls
        n= len(position)
        left = 1
        right = position[-1] - position[0]
        ans = 0

        while (left <= right):
            mid = (left + right)//2

            if self.canPlace(position , mid , m):
                ans = mid
                left = mid +1
            else:
                right = mid -1
        
        return ans
    
    def canPlace(self, position: list[int], distance : int , balls : int) -> bool:

        lastPlaced = position[0] #placing the first ball at earliest as possible (greedy)
        placed = 1

        for i in range(1, len(position)):
            if position[i] - lastPlaced >= distance:
                placed += 1
                lastPlaced = position[i]

                if placed == balls:
                    return True
        
        return False