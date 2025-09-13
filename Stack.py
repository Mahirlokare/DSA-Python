class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

s = Stack()
s.push(10)
s.push(20)
print(s.pop())   # 20
print(s.peek())  # 10
