class Largest_Element:

    def __init__(self):
        pass
    

    #using index
    def largest(self,arr: list[int]) -> int:

        if not arr:
            raise ValueError("Array is empty")
        max_index = 0
        for i in range(len(arr)):
            if arr[i] > arr[max_index]:
               max_index = i
        
        max_element = arr[max_index]
        return max_element
    

    #using iterables, pythonic
    def largest1(self,arr: list[int]) -> int:

        if not arr:
            raise ValueError("Array is empty")
        
        max_element = arr[0]
        for i in arr:
            if i > max_element:
               max_element = i

        return max_element
    

    #using in built function
    def largest2(self,arr: list[int]) -> int:
        return max(arr)


if __name__ == "__main__":
    obj = Largest_Element()
    print(obj.largest2([2,6,1,4,9,0,7,-1]))