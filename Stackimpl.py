class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack Underflow"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Empty Stack"

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
n = int(input("Enter number of stack operations: "))
for _ in range(n):
    op = input("Enter operation (push x / pop / peek): ").split()
    if op[0] == "push":
        stack.push(int(op[1]))
    elif op[0] == "pop":
        print("Popped:", stack.pop())
    elif op[0] == "peek":
        print("Top:", stack.peek())

# Complexity:
# Push/Pop/Peek: O(1)
