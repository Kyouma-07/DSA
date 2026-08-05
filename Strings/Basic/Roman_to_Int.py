class LC13:
    def romanToInt(self, s: str) -> int:
        
        mapping = {
            "I" : 1,
            "V" : 5,
            "X" :10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        n = len(s)
        res = [mapping[s[-1]]]

        for i in range(len(s)-2, -1 , -1):
            mapping[s[i]]

            if mapping[s[i]] < mapping[s[i+1]]:
                 res.append(-mapping[s[i]])
            else:
               res.append(mapping[s[i]])
        
        total = 0
        for i in range(len(res)):
            total += res[i]
        
        return total