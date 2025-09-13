#Brute force: 
#Time: O(n) for getMin, O(1)  for other operations
#Space: O(n) for getMin, O(1)  for other operations

class MinStack:

    def __init__(self):
        self.content = []

    def push(self, val: int) -> None:
        self.content.append(val)

    def pop(self) -> None:
        self.content.pop()

    def top(self) -> int:
        return self.content[-1]

    def getMin(self) -> int:
        return min(self.content) #this is still O(n), not O(1)
        
#Optimized, O(n) for getMin:
class MinStack:
    #use a stack to maintain the minimum value at the same index as default stack 
    def __init__(self):
        self.content = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.content.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        current = self.content.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.content[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
