from queue import Queue
import time

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
    c = int(input("Enter the choice:"))
    if c in (1, 2, 3, 4, 5):
        if (c == 5):
            break
        if (c==1):
            if(queue.full()):
                print("Queue is full already!")
                time.sleep(3)
            else:
                d = int(input("Enter the data:"))
                queue.put(d)
        elif (c==2):
            if(not queue.empty()):
                ("Dequeued element is",queue.get())
                time.sleep(3)
            else:
                print("Queue is empty, can not dequeue")
        elif (c==3):
            print("Queue =",list(queue.queue))
            time.sleep(3)
        elif (c==4):
            while not queue.empty():
                queue.get()
            print("Queue cleared")
            time.sleep(3)
    else:
        print("Invalid Choice, please try again")
        time.sleep(3)