class NthRoot:

    def __init__ (self):
        pass

    def nthRoot(self,n: int, m: int) -> int:

        left = 1
        right = n

        while left <= right:

            mid = (left + right) // 2
            power = mid ** m

            if power == n:
                return mid

            elif power < n:
                left = mid + 1

            else:
                right = mid - 1

        return -1