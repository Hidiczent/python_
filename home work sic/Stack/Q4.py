

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

    def clear(self):
        self.stack.clear()
        print("Stack cleared")

    def display(self):
        print("Stack =", self.stack)

stack = Stack()

while True:
    print("\n")
    print("========================")
    print("Manage Stack Program")
    print("1. Push data")
    print("2. Pop data")
    print("3. Display the value of stack")
    print("4. Clear stack")
    print("5. Exit the program")
    print("========================")
    choice = int(input("Enter the choice:"))
    if choice in (1, 2, 3, 4, 5):
        if (choice == 5):
            break
        if (choice == 1):
            if len(stack.stack) >= 5:
                print("Stack is full already!")
    
            else:
                data = int(input("Enter the data:"))
                stack.push(data)
        elif (choice == 2):
            data = stack.pop()
            if data is None:
                print("Stack is empty, can not pop")
            else:
                print("Pop element is", data)
    
        elif (choice == 3):
            stack.display()

        elif (choice == 4):
            stack.clear()

        else:
            print("Invalid Choice, please try again")
