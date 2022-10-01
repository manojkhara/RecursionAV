# stack Last in first out

def sortStack(arr):
    if len(arr) <= 1 :    # if there is only one element in stack than its sorted
        return
    num = arr.pop()      # if not 
    sortStack(arr)

    # insert function will put num at right position in sorted stack
    def insert(arr,num):
        if arr == [] or arr[len(arr)-1] < num: 
            arr.append(num)
            return
        temp = arr.pop()   # stored the top element because it was bigger than num
        insert(arr,num)    # again checking if num can be appended at top
        arr.append(temp)   # after sorting remaining element in stack, add the temp 
    
    insert(arr,num)


stack =[5,3,2,4,-5,1,6,-1,9,0]
sortStack(stack)
print(stack)

