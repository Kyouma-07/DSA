class LC1593:
    def maxUniqueSplit(self, s: str) -> int:
        used = set()

        def backtrack(index : int):
            
            #reached end of string : no more to count
            if index == len(s):
                return 0
            
            ans = 0
            
            #iterating through string:
            for i in range(index + 1 , len(s) + 1):

                #creating substrings
                sub = s[index : i]
                
                #checking if in set
                if sub not in used:
                    #add to set
                    used.add(sub)

                    #update ans:
                    ans = max(ans , 1 + backtrack(i))

                    #remove:
                    used.remove(sub)
            
            return ans
        
        return backtrack(0)
       