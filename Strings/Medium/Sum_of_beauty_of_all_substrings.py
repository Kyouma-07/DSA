class LC1781:
    def beautySum(self, s: str) -> int:
        
        if not s:
            return 0


        n = len(s)
        total_beauty = 0


        #generate all possible susbtrings:
        for i in range(n):

            freq = [0]*n  #using an array instead of map
            for j in range(i, n):

                idx = ord(s[j]) - ord('a')
                freq[idx] += 1


                max_freq = 0
                min_freq = float('inf')   

                for f in freq:
                    if f > 0:
                        max_freq = max(max_freq, f)
                        min_freq = min(min_freq , f)

                total_beauty += (max_freq - min_freq)
        
        return int(total_beauty)
