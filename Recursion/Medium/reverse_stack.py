def reverseStack(stack):

    if not stack:
        return 

    val = stack.pop()
    print(f"popped value :  {val}")

    print(f"stack :  {stack}\n")
    reverseStack(stack)

    print(f"insert into this stack: {stack}\n")
    insertBottom(stack, val)

def insertBottom(stack, val):

    if not stack:
        stack.append(val)
        return


    #remove top temporarily
    top = stack.pop()
    print(f"removing- top:  {top}\n")

    #go depper:
    print(f"going deeper:   {stack}\n")
    insertBottom(stack, val)

    #append top:
    print(f"appending top:  {top}\n")
    stack.append(top)

stack = [5, 4, 3, 2, 1]

reverseStack(stack)

print(stack)