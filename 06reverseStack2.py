# input  => deque([2, 1, 8, 1, 5, 11])
# output => deque([11, 5, 1, 8, 1, 2])

from collections import deque

stack = deque()

stack.append(2)
stack.append(1)
stack.append(8)
stack.append(1)
stack.append(5)
stack.append(11)

print(stack)
stack.reverse()
print(stack)