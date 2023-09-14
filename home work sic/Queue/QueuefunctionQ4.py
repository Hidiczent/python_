
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue.clear()
        print("Queue cleared")

    def display(self):
        print("Queue =", self.queue)


queue = Queue()

while True:
    print("\n")
    print("========================")
    print("Manage Queue Program")
    print("1. Enqueue data")
    print("2. Dequeue data")
    print("3. Display the value of queue")
    print("4. Clear queue")
    print("5. Exit the program")
    print("========================")
    choice = int(input("Enter the choice:"))
    if choice in (1, 2, 3, 4, 5):
        if (choice == 5):
            break
        if (choice == 1):
            if len(queue.queue) >= 5:
                print("Queue is full already!")
            else:
                data = int(input("Enter the data:"))
                queue.enqueue(data)
        elif (choice == 2):
            data = queue.dequeue()
            if data is None:
                print("Queue is empty, can not dequeue")
            else:
                print("Dequeued element is", data)

        elif (choice == 3):
            queue.display()
        elif (choice == 4):
            queue.clear()
        else:
            print("Invalid Choice, please try again")
