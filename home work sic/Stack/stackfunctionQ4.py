class Stack:
    def __init__(self):
        self.items = {}
    def push(self,key,value):
        if not  self.is_full():
            print(f" ເພິ່ມ key {key} ເຂົ້າ Stack ສຳເລັດແລ້ວ")
            self.items[key]=value
        else:
            print('Stack ເຕັມແລ້ວ ')
    def pop (self,key):
        if not self.is_empty():
            if key in self.items:
                value = self.items.pop(key)
                print(f"ນຳເອົາkey {key} ອອກຈາກ Stackສຳເລັດແລ້ວ")
                return value
            else:
                print('ບໍ່ພົບ key')
        else:
            print('Stack ວ່າງ')

    def is_full(self):
        return len(self.items)==10
    
    def is_empty(self):
        return not self.items
    
    def clear(self):
        self.items.clear()
    

stack=Stack()

while True:
    print('\n')
    print('=========================')
    print(' ຈັດການໂຄງການ Stack ')
    print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ Stack: ')
    print('2. ເອົາຂໍ້ມູນອອກ Stack:')
    print('3. ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ Stack: ')
    print('4.ກວດສອບ Stack ວ່າເຕັມຫຼືບໍ່: ')
    print('5.Clear stack')
    print('6.ອອກຈາກໂປຣແກຣມ')
    print("========================")

    choice =int(input('ເລືອກສິ່ງທີ່ຕ້ອງການ: '))

    if choice in (1,2,3,4,5,6):
        if (choice==1):
            key=input('ປ້ອນkey: ')
            value=input('ປ້ອນvalue: ')
            stack.push(key,value)
        elif (choice==2):
            key=input('ນຳເອົາkeyອອກ: ')
            stack.pop(key)
        elif (choice == 3):
            print('Stack ',stack.items)
        elif (choice == 4 ):
            if stack.is_full():
                print('Stack ເຕັມແລ້ວ')
            else:
                print('Stackຍັງບໍເຕັມ')
        elif (choice ==5 ):
            stack.clear()
            print('Stack cleared.')
        
        elif (choice == 6):
            break
    else:
        print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງn")
