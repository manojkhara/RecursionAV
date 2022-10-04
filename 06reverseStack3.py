from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def reverseStack(self):
        if self.size() == 1:
            return

        temp = self.pop()
        self.reverseStack()
        self.insert(temp)
    
    def insert(self,num):
        if self.is_empty() :
            self.push(num)
            return
        temp = self.pop()
        self.insert(num)
        self.push(temp)

    def printStack(self):
        for i in range(1,self.size()+1):
            print(self.container[-i])





st = Stack()

# input  => deque([2, 1, 8, 1, 5, 11])
# output => deque([11, 5, 1, 8, 1, 2])

st.push(2)
st.push(1)
st.push(8)
st.push(1)
st.push(5)
st.push(11)

print("Stack")
print(st.printStack())

st.reverseStack()

print("\nReverse Stack")
print(st.printStack())