class LC2904:

    def __init__ (self):
        pass

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):

            #expand window:
            if s[right] == "1":
                ones += 1
            
            #shink if ones > k
            while ones > k:
                if s[left] == "1":
                    ones -= 1
                left += 1

            #if k == ones => beautiful string:
            if ones == k:

                #remove zeros if necessary:
                while s[left] == "0":
                    left += 1
                
                current = s[left: right +1]

                #updating ans:
                if ans == "":
                    ans = current
                elif len(current) < len(ans):
                    ans = current
                elif len(current) == len(ans) and current < ans:
                    ans = current
        
        return ans