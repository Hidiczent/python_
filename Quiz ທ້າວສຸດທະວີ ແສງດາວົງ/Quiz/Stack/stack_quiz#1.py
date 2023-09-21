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

stack.push("Banana")
stack.push("Apple")
stack.push("Tomato")
stack.pop()
stack.push("Strawberry")
stack.push("Grapes")
stack.pop()
print(stack.stack)

# Output : ['Banana', 'Apple', 'Strawberry']