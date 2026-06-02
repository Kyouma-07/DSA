class LC48:

    def __init__(self):
        pass

    def rotate(self, matrix: list[list[int]]):
        
        n = len(matrix)
        #given matrix is n*n sq matrix
        res = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][n-i-1] = matrix[i][j]
        
        return res

    def rotateOptimal(self, matrix: list[list[int]]):
         n = len(matrix)

         #transposing the matrix
         for i in range(n):
             for j in range(i,n):
                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #reversing the matrix
         for row in matrix:
             row.reverse()
        