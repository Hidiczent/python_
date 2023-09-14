from collections import deque
queue = deque()

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
            if(len(queue)>5):
                print("Queue is full already!")
             
            else:
                data = int(input("Enter the data:"))
                queue.append(data)
        elif (choice==2):
            if(len(queue)>=1):
                print("Dequeued element is",queue.popleft())
             
            else:
                print("Queue is empty, can not dequeue")
        elif (choice==3):
            print("Queue =",queue)
         
        elif (choice==4):
            queue.clear()
            print("Queue cleared")
         
    else:
        print("Invalid Choice, please try again")
     