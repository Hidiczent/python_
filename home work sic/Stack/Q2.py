from collections import deque
stack = deque()
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
    if choice in (1, 2, 3, 4,5):
        if (choice == 5):
            break
        if (choice==1):
            if(len(stack)>5):
                print("Stack is full already!")
    
            else:
                d = int(input("Enter the data:"))
                stack.append(d)
        elif (choice==2):
            if(len(stack)>=1):
                 item = stack.pop()
                 print(f" ນຳເອົາ {item} ອອກຈາກ Stackສຳເລັດແລ້ວ ")
            else:
                print("Stack is empty, can not pop")
        elif (choice==3):
            print("Stack =",stack)

        elif (choice==4):
            stack.clear()
            print("Stack cleared")

    else:
        print("Invalid Choice, please try again")