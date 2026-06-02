class LC73:

    def __init__(self):
        pass

    #works only for binary matrix
    def setZeroes5(self, matrix :list[list[int]]) -> None:

        n = len(matrix) #no. of rows
        m = len(matrix[0]) #no. of columns

        if n == 0:
            return
        
        #helper row
        def setRow(i):
            for col in range(m):
                if matrix[i][col] == 1:
                    matrix[i][col] = -1
        #helper col
        def setCol(j):
            for row in range(n):
                if matrix[row][j] == 1:
                    matrix[row][j] = -1
            
        #setting up array val
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    setRow(i)
                    setCol(j)
        
        #converting -1 to 0 again
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
    
    #for any matrix
    def setZeroes1(self, matrix :list[list[int]]) -> None:

        n = len(matrix)
        m = len(matrix[0])

        if n == 0:
            return

        rows= set()  #using set cause [i][j] (cell) are always unique but i,j ( row , column ) indices are not unique across zero
        col = set()  # for matrix [[101], [101]] here row got two val = 0,1 , but column is same 1,1 , so we store only 1

        #finding indeces where value is 0
        for i in range(n):
            for j in range (m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    col.add(j)
        
        #setting the values to 0
        for i in range(n):
            for j in range(m):
                if i in rows or j in col:
                    matrix[i][j] = 0

    #optimal 0(1) space
    def setZeroes2(self, matrix : list[list[int]]) -> None:

        if not matrix or not matrix[0]:
            return
        
        n = len(matrix)
        m = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        #check first row for 0
        for j in range(m):
            if matrix[0][j] == 0:
                firstRowZero = True
                break
        
        #check first col for 0
        for i in range(n):
            if matrix[i][0] == 0:
                firstColZero = True
                break
        
        #updating  (using 1st row and col as markers)
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        #updating innermatrix
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        #updating first row
        if firstRowZero:
            for j in range(m):
                matrix[0][j] = 0
        
        #updating first col
        if firstColZero:
            for i in range(n):
                matrix[i][0] = 0
    

    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        col0 = True

        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = False
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in reversed(range(rows)):
            for j in reversed(range(1, cols)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if not col0:
                matrix[i][0] = 0
        
                   

    
