#%% #10828
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름
class Stack:
    def __init__(self):
        self.stack = []    

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        else:
            result = self.stack[-1]
            self.stack.pop()
            return result

    def size(self):
        return len(self.stack)

    def empty(self):
        if not self.stack:
            return 1
        else:
            return 0

    def top(self):
        if not self.stack:
            return -1
        else:
            return self.stack[-1]

N =  int(input())
myStack = Stack()
for i in range(N):
    commend = input().split()
    if commend[0] == "push":
        myStack.push(commend[1])
    elif commend[0] == "pop":
        print(myStack.pop())
    elif commend[0] == "size":
        print(myStack.size())
    elif commend[0] == "empty":
        print(myStack.empty())
    elif commend[0] == "top":
        print(myStack.top())
    else:
        print("error")