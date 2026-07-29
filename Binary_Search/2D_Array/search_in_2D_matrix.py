class LC74:

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
    
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows - 1

        while low <= high:

            mid = (low + high) // 2

            # Is the target in this row?
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:

                left = 0
                right = cols - 1

                while left <= right:

                    mid_col = (left + right) // 2

                    if matrix[mid][mid_col] == target:
                        return True
                    elif matrix[mid][mid_col] < target:
                        left = mid_col + 1
                    else:
                        right = mid_col - 1

                return False

            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        return False


    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2

            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
    
