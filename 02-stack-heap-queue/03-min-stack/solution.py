#! /usr/bin/python

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if self.stack[-1] <= self.min_stack[-1]:
                self.min_stack.append(self.stack[-1])
        else:
            self.min_stack.append(self.stack[-1])

    def pop(self) -> None:
        element = self.stack.pop()
        if element == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

if __name__ == "__main__":
    pass
