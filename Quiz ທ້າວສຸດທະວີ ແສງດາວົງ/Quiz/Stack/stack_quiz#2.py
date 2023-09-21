class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
items = [10 * i for i in range(1,10)]
for item in items:
    stack.push(item)
    if (item // 10) % 2 == 0 :
        stack.pop()

print(stack.stack)

# Output : [10, 30, 50, 70, 90]