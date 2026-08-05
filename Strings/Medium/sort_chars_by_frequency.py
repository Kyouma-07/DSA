class LC451:
    def frequencySort(self, s: str) -> str:
        
        result = []
        n= len(s)

        freq = {}

        #STORE ALL freq in hashmap
        for i in s:
            freq[i] = freq.get(i, 0) + 1

        #create n +1 buckets
        buckets = [[] for _ in range(n+1)]

        #put characters in bucket based on their frequencies
        for ch , count in freq.items():
            buckets[count].append(ch)

        #traverse the bucket backwards (descending order)
        for i in range(len(buckets)-1,0 , -1):
            for ch in buckets[i]:
                result.append(ch*i)
        
        return "".join(result)


    def frequencySort2(self, s: str) -> str:
        
        freq ={}
        result = []


        #store all the frequencies in a hashmap
        for i in s:
            freq[i] = freq.get(i,0) + 1
        
        keys = sorted(freq, key=lambda x: freq[x], reverse=True)

        for key in keys:
            times = freq[key]
            result.append(key*times)

        res = "".join(result)
        return res
        