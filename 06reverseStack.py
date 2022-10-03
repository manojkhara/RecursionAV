# Reverse a Stack
#input = [2,4,3,1,0]   ==> output = [0,1,3,4,2]

def reverseStack(stack):
    if len(stack) == 1 :
        return
    
    temp = stack.pop()
    reverseStack(stack)
    insert(stack,temp)

def insert(stack,num):
    if stack == []:
        stack.append(num)
        return
    temp = stack.pop()
    insert(stack,num)
    stack.append(temp)

stack = [2,4,3,1,0]
reverseStack(stack)
print(stack)
