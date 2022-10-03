# stack Last in first out

def sortStack(stack):
    if len(stack) <= 1 :    # if there is only one element in stack than its sorted
        return
    num = stack.pop()      # if not 
    sortStack(stack)

    # insert function will put num at right position in sorted stack
    def insert(stack,num):
        if stack == [] or stack[len(stack)-1] < num: 
            stack.append(num)
            return
        temp = stack.pop()   # stored the top element because it was bigger than num
        insert(stack,num)    # again checking if num can be appended at top
        stack.append(temp)   # after sorting remaining element in stack, add the temp 
    
    insert(stack,num)


stack =[5,3,2,4,-5,1,6,-1,9,0]
sortStack(stack)
print(stack)

