class Second_Largest:

    def __init__(self):
        pass


    def find_element(self, arr: list[int]):

        # if length of array is < 2, it should have no 2nd largest element
        if len(arr) < 2:
            return None

        largest = arr[0]
        second_largest = float('-inf')

        for i in range(1,len(arr)):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            elif arr[i] > second_largest and arr[i] != largest:   # if the element is > second_largest but is != largest , we swap (handles -ve value too)
                # if largest > arr[i] > second_largest also works
                second_largest = arr[i]
        
        return second_largest if second_largest != float('-inf') else None

if __name__ == "__main__":
    obj = Second_Largest()
    print(obj.find_element([2,6,1,4,9,0,7,-1]))


#same logic can be applied to smallest element and 2nd smallest element.