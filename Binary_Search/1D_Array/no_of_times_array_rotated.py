class Rotation:

    def __init__(self):
        pass

    def rotationCount(self, arr: list[int]) -> int:

        left = 0
        right = len(arr) - 1
        answer = 0

        while left <= right:

            # Current interval is sorted
            if arr[left] <= arr[right]:
                if arr[left] < arr[answer]:
                    answer = left
                break

            mid = (left + right) // 2

            # Left half is sorted
            if arr[left] <= arr[mid]:
                if arr[left] < arr[answer]:
                    answer = left
                left = mid + 1

            # Right half is sorted
            else:
                if arr[mid] < arr[answer]:
                    answer = mid
                right = mid - 1

        return answer