class LC765:
    def minSwapsCouples(self, row: list[int]) -> int:
        swaps = 0
        n = len(row)
        swaps = 0

        position = {}

        #key-> row , value -> idx
        for i in range(n):
            person = row[i]
            position[person] = i 
        

        for i in range(0, n, 2):
            person = row[i]
            partner = person ^ 1

            # if they sitting together
            if partner == row[i+1]:
                continue
            
            #if not , find the position of the partner
            j = position[partner]
            #next person sitting with person
            other = row[i+1]

            #swap these 2
            row[i+1], row[j] = row[j], row[i+1]

            #update position in the dict:
            position[partner] = i+1
            position[other] = j


            swaps += 1
        
        return swaps


