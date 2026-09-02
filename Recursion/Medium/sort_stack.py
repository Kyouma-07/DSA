def sortStack(stack):
    # Base case
    if not stack:
        return
    
    val = stack.pop()
    sortStack(stack)

    insertSorted(stack, val)


def insertSorted(stack, val):

    if not stack or val >= stack[-1]:
        stack.append(val)
        return

    top = stack.pop()
    insertSorted(stack, val)
    stack.append(top)



stack = [5, 4, 3, 2, 1]

sortStack(stack)

print(stack)