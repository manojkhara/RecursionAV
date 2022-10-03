# Delete Middle Element of a Stack
# middle element = (size of stack /2) + 1
# input  = [1,3,5,7,4]  ===>  output = [1,3,7,4]
# input = [0,6,2,7]  ==>   output = [0,2,7]

def delMiddleElement(stack,mid):        
    if mid == 1:
        stack.pop()
        return
    temp = stack.pop()
    delMiddleElement(stack,mid-1)
    stack.append(temp)

# driver code
# stack = [1,3,5,7,4]
stack = [0,6,2,7]

mid = len(stack)//2 + 1
delMiddleElement(stack,mid)
print(stack)