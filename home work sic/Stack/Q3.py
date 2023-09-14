from queue import LifoQueue


# create a stack queue
stackq = LifoQueue()

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
        if (choice==1):
            if(stackq.qsize()>5):
                print("Stack is full already!")
              
            else:
                d = int(input("Enter the data:"))
                stackq.put(d)
        elif (choice==2):
            if(stackq.qsize()>=1):
                    data = stackq.get()
                    print(f" ນຳເອົາ {data} ອອກຈາກ Stackສຳເລັດແລ້ວ ")
             
              
            else:
                print("Stack is empty, can not pop")
        elif (choice==3):
            print("Stack =",list(stackq.queue))
          
        elif (choice==4):
            while not stackq.empty():
                stackq.get()
            print("Stack cleared")
          
    else:
        print("Invalid Choice, please try again")
      