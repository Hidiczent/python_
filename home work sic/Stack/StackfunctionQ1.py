
class Stack:
    def __init__(self):
        self.items = []
        self.max_size = 5

    def push(self, item):
        if len(self.items) >= self.max_size:
            print("Stack is full!")
        else:
            self.items.append(item)
            print(f"{item} added to stack")

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty!")
        else:
            item = self.items.pop()
            print(f"{item} removed from stack")

    def is_full(self):
        return len(self.items) == self.max_size

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []
        print("Stack is cleared")

stack = Stack()

while True:
    print("\n")
    print("Stack Management Menu")
    print("--------------------------")
    print("1. Add data to stack")
    print("2. Remove data from stack")
    print("3. Check if stack is full")
    print("4. Check if stack is empty")
    print("5. Clear stack")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter data to add to stack: ")
        stack.push(item)
    elif choice == "2":
        stack.pop()
    elif choice == "3":
        if stack.is_full():
            print("Stack is full")
        else:
            print("Stack is not full")
    elif choice == "4":
        if stack.is_empty():
            print("Stack is empty")
        else:
            print("Stack is not empty")
    elif choice == "5":
        stack.clear()
    elif choice == "6":
        break
    else:
        print("Invalid choice! Please try again.")
