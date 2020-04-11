class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        curMin = x
        if self.stack:
            preMin = self.stack[-1][1]
            if x > preMin:
                curMin = preMin
        self.stack.append([x, curMin])

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()[0]
        else:
            return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None

# One possible optimization is to store MIN and curValue to the stack

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()