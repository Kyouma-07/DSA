class Leaders:

    def __init__ (self):
        pass

    def leader_arr(self, arr : list[int]) -> list[int]:

        max_val = arr[-1]
        result = [max_val]

        n= len(arr)

        for i in range(n-2, -1 , -1):
            if arr[i] > max_val:
                result.append(arr[i])
                max_val = arr[i]

        return result
    

if __name__ == "__main__":
    print("hello world")
    obj = Leaders()
    print(obj.leader_arr([10,22, 12, 3, 0, 6]))
