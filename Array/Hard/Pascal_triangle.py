class LC118:

    def __init__(self):
        pass
    
    def pascals_triangle(self, n: int):

        triangle = [[1]]
        for i in range (1 , n):
             row = [1]
             prev = triangle[i-1]   #triangle[-1] works cause we fetch last row.

             for j in range(len(prev)-1):
                 row.append(prev[j] + prev[j+1])
            
             row.append(1)
             triangle.append(row)
        
        return triangle

    def print_triangle(self, triangle):
         n = len(triangle)

         for i in range(n):
             print(" " * (n-i), end =" ")

             for num in triangle[i]:
                 print(num, end= " ")

             print()

    def returnIndexVal(self, row: int, col : int) -> int:
         val = 1
         #val = C(row, i) for row = 1, col = 1=> val = 1
         for i in range(col):
             val = val * (row-i) // (i+1)
         return val
    
    def returnRow(self, row: int) -> list[int]:

        answer = [1]
        val = 1

        for i in range(1, row+1):
            val = val * (row-i) // (i+1)
            answer.append(val)
        answer.append(1)

        return answer


if __name__ ==  "__main__":
    print("Pascal's Traingle")
    obj1 = LC118()
    tri = obj1.pascals_triangle(5)
    obj1.print_triangle(tri)