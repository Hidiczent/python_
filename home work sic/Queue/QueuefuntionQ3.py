from queue import Queue


# create a queue
queue = Queue(max=5)

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
        if (choice==1):
            if(queue.full()):
                print("Queue is full already!")
            else:
                data = int(input("Enter the data:"))
                queue.put(data)
        elif (choice==2):
            if(not queue.empty()):
                ("Dequeued element is",queue.get())
            else:
                print("Queue is empty, can not dequeue")
        elif (choice==3):
            print("Queue =",list(queue.queue))
        
        elif (choice==4):
            while not queue.empty():
                queue.get()
            print("Queue cleared")
        
    else:
        print("Invalid Choice, please try again")
    