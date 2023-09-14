
Stack= []
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
    print("========================")
    choice = int(input("Enter the choice:"))
    if choice in (1, 2, 3, 4, 5 ,6):
        if (choice==1):
              if len(Stack)==5:
                  print(' Stack ເຕັມແລ້ວ ')
              else:
                    item=int(input('ປ້ອນຂໍ້ມູນລົງໃນ Stack :'))
                    Stack.append(item)
        elif (choice==2):
            if len (Stack)==0:
                print('Stack ວ່າງ')
            else:
                 item = Stack.pop()
                 print(f" ນຳເອົາ {item} ອອກຈາກ Stackສຳເລັດແລ້ວ ")
        elif (choice==3):
             print('Stack' ,Stack)

        elif (choice ==4):
                print('queue ຍັງບໍ່ເຕັມ')
        elif (choice == 5):
                Stack.clear()
                print('queue cleared.')
        elif (choice == 6):
                break
    else:
        print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງn")
       
