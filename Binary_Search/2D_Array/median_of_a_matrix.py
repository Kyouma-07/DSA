from bisect import bisect_right

def median(matrix, R, C):
    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)
    desired = (R * C) // 2

    while low <= high:
        mid = (low + high) // 2

        count = sum(bisect_right(row, mid) for row in matrix)

        if count <= desired:
            low = mid + 1
        else:
            high = mid - 1

    return low