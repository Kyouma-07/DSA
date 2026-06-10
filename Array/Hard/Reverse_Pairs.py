from typing import List

class Solution:
    def reversePairs(self, arr: List[int]) -> int:
        return self.mergesort(arr, 0, len(arr) - 1)

    def mergesort(self, arr: List[int], left: int, right: int):
        if left >= right:
            return 0

        mid = (left + right) // 2

        count = 0
        count += self.mergesort(arr, left, mid)
        count += self.mergesort(arr, mid + 1, right)
        count += self.countInversion(arr, left, mid, right)

        self.merge(arr, left, mid, right)

        return count 

    def merge(self, arr: List[int], left: int, mid: int, right: int):
        i = left
        j = mid + 1
        temp = []

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:   
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])  
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

       
        for k in range(len(temp)):
            arr[left + k] = temp[k]  

    def countInversion(self, arr: List[int], left: int, mid: int, right: int):
        count = 0
        j = mid + 1

        for i in range(left, mid + 1):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += (j - (mid + 1))

        return count