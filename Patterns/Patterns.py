#STEP 1 :   for outer loop count the number of lines:-> determine the number of lines.
#STEP 2 :   for the inner loop -> foucs on the columns and connect them somehow to the rows.
#STEP 3 :   whatever we are pritning we need to print them inside the inner for loop.
#STEP 4 :   observer symmetry in case of some patterns (optional).


class Patterns:

    def __init__(self):
        pass


    def pattern1(self , n : int):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print("\n")

    def pattern2(Self , n : int):
        for i in range(1,n+1):
            for j in range(1,n+1):
                print("*",end=" ")
            print("\n")

    def pattern3(Self , n : int):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print("\n")

    def pattern4(Self , n:  int):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end=" ")
            print("\n")

    def pattern5(Self , n:  int):
        for i in range(1,n+1):
            for j in range(i,n+1):
                print("*",end=" ")
            print("\n")

    def pattern6(Self , n:  int):
        for i in range(1,n+1):
            for j in range(1,n+2-i):
                print(j,end=" ")
            print("\n")

    def pattern7(Self, n:   int):
        for i in range(1,n+1):
            for j in range(1,n+2-i):
                print(i,end=" ")
            print("\n")

    def pattern8(Self, n:   int):
        for i in range(1,n+1):
            #space
            for j in range(1,n+2-i):
                print(" ",end=" ")

            #star
            for j in range(1,2*i):
                print("*",end=" ")

            #space
            for j in range(1,n+2-i):
                print(" ",end=" ")

            print("\n")

    def pattern9(Self, n:   int):
        for i in range(1,n+1):
            #space
            for j in range(1,i):
                print(" ",end=" ")

            #star
            for j in range(1,2*n-2*i+2):
                print("*",end=" ")

            #space
            for j in range(1,i):
                print(" ",end=" ")

            print("\n")

    def pattern10(Self, n:  int):
        for i in range(1,n+1):
            #space
            for j in range(1,n+2-i):
                print(" ",end=" ")

            #star
            for j in range(1,2*i):
                print("*",end=" ")

            #space
            for j in range(1,n+2-i):
                print(" ",end=" ")

            print("\n")
        
        for i in range(1,n+1):
            #space
            for j in range(1,i):
                print(" ",end=" ")

            #star
            for j in range(1,2*n-2*i+2):
                print("*",end=" ")

            #space
            for j in range(1,i):
                print(" ",end=" ")

            print("\n")

    def pattern11(Self , n: int):
        for i in range (1, n+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print("\n")

        for i in range(1,n+1):
            for j in range(1,n+1-i):
                print("*",end=" ")
            print("\n")

    def pattern12(Self , n: int):
        start = 1
        for i in range (1, n+1):
            if(i%2==0):
                start = 0
            else:
                start = 1
            for j in range(1,i+1):
                print(start,end=" ")
                start = 1 - start
            print("\n")

    def pattern13(Self , n: int):
        space = 2*(n-1)
        for i in range(1,n+1):

            #numbers
            for j in range(1,i+1):
                print(j,end=" ")
            
            
            #space
            for j in range(1,space):
                print(" ",end=" ")

            #numbers
            for j in range(i,0,-1):
                print(j,end=" ")
            print("\n")
            space -= 2

    def pattern14(Self , n: int):
        count = 1
        for i in range ( 1, n+1):
            for j in range(1,i+1):
                print(count,end=" ")
                count += 1
            print("\n")

    def pattern15(Self , n: int):
        for i in range (n):
            for j in range(i+1):
                print(chr(65+j),end=" ")
            print("\n")

    def pattern16(Self , n: int):
        for i in range (n):
            for j in range(i+1):
                print(chr(65+i),end=" ")
            print("\n")
    
    def pattern17(Self , n: int):
        for i in range (n):
            for j in range(i+1):
                print(chr(65+n-i-1),end=" ")
            print("\n")

    def pattern18(Self , n: int):
        for i in range (n):
            for j in range(i+1):
                print(chr(65+n-j-1),end=" ")
            print("\n")

    def pattern19(Self , n: int):
        for i in range (n):
            for j in range(n-i):
                print(chr(65+j),end=" ")
            print("\n")
        
    def pattern20(Self , n: int):
        for i in range (n):
            for j in range(n-i):
                print(chr(65+i),end=" ")
            print("\n")

    def pattern21(Self , n: int):
        for i in range (n):
            #space
            for j in range(n-i-1):
                print(" ",end=" ")       
            #chars
            a = 65
            breakpoint = (2*i+1)//2
            for j in range(2*i+1):
                print(chr(a),end=" ")
            
                if(j < breakpoint):
                    a += 1
                else:
                    a -= 1
            #space
            for j in range(n-i-1):
                print(" ",end=" ")
            
            print("\n")

    def pattern22(Self , n: int):
        for i in range (n):
            for j in range(i,-1,-1):
                print(chr(65+n-j-1),end=" ")
            print("\n")

    def pattern23(Self , n: int):

        space = 0
        for i in range (n):

            #star
            for j in range(n-i):
                print("*",end=" ")

            #space
            for j in range(2*space):
                print(" ",end=" ")
            
            #star
            for j in range(n-i):
                print("*",end=" ")
            
            print("\n")

            space += 1
        
        num = 8
        for i in range (n):
            #star
            for j in range(i+1):
                print("*",end=" ")

            #space
            for j in range(num):
                print(" ",end=" ")

            #star
            for j in range(i+1):
                print("*",end=" ")

            print("\n")

            num = num-2

    def pattern24(Self , n: int):
        num = 8
        for i in range (n-1):
            #star
            for j in range(i+1):
                print("*",end=" ")

            #space
            for j in range(num):
                print(" ",end=" ")

            #star
            for j in range(i+1):
                print("*",end=" ")

            print("\n")

            num = num-2

        space = 0
        for i in range (n):

            #star
            for j in range(n-i):
                print("*",end=" ")

            #space
            for j in range(2*space):
                print(" ",end=" ")
            
            #star
            for j in range(n-i):
                print("*",end=" ")
            
            print("\n")

            space += 1
        
    def pattern25(Self , n: int):
        for i in range(n):
            for j in range(n):
                if (i ==0 or j==0 or i==n-1 or j==n-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("\n")

    def pattern26(Self , n: int):
        for i in range(2*n-1):
            for j in range(2*n-1):
                top = i
                left = j
                right = (2*n-1)-1-j
                bottom = (2*n-1)-1-i
                print(4-(min(top,left,right,bottom)),end=" ")

            print("\n")


if __name__ == "__main__":

    print("Select the pattern you want to print:")

    n = int(input("Enter the number of rows:"))
    pattern = Patterns()
    #pattern.pattern1(n)
    #pattern.pattern2(n)
    #pattern.pattern3(n)
    #pattern.pattern4(n)
    #pattern.pattern5(n)
    #pattern.pattern6(n)
    #pattern.pattern7(n)
    #pattern.pattern8(n)
    #pattern.pattern9(n)
    #pattern.pattern10(n)
    #pattern.pattern13(n)
    #pattern.pattern14(n)
    #pattern.pattern15(n)
    #pattern.pattern16(n)
    #pattern.pattern17(n)
    #pattern.pattern18(n)
    #pattern.pattern19(n)
    #pattern.pattern20(n)
    #pattern.pattern21(n)
    #pattern.pattern22(n)
    #pattern.pattern23(n)
    #pattern.pattern24(n)
    #pattern.pattern25(n)
    pattern.pattern26(n)