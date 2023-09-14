from collections import deque
class Stack:
    def __init__(self):
        self.items=deque(maxlen=10)
    def push(self,items):
        if not self.is_full():
            print(f" ເພິ່ມ {item} ເຂົ້າ Stack ສຳເລັດແລ້ວ")
            self.items.append(items)
        else:
            ('Stack ເຕັມແລ້ວ.')
    def pop(self):
        if not self.is_empty():
            print(f" ນຳເອົາ {item} ອອກຈາກ Stackສຳເລັດແລ້ວ ")
            return self.items.pop()
        else:
           print('Stack ວ່າງ')
    def is_full(self):
        return len(self.items) == self.items.maxlen
    def is_empty(self):
        return len(self.items) == 0
    def clear(self):
        self.items.clear()

stack = Stack()

while True: 
        print('\n')
        print('=========================')
        print(' Stack Management Menu ')
        print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ Stack: ')
        print('2.ດຶງຂໍ້ມູນອອກ Stack:')
        print('3.ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ Stack:')
        print('4.ກວດສອບ Stack ວ່າເຕັມຫຼືບໍ່: ')
        print('5.Clear stack')
        print('6.ອອກຈາກໂປຣແກຣມ')
        data = int(input('Enter your choice: '))
        if data in (1,2,3,4,5,6):
            if data == 1:
                item = input(' ເພິ່ມຂໍ້ມູນເຂົ້າStack ')
                stack.push(item)
            elif data == 2:
                stack.pop()
            elif data == 3:
                print('Stack = ', stack.items)
            elif data == 4:
                if stack.is_full():
                    print('Stackເຕັມແລ້ວ')
                else:
                    print('Stackຍັງບໍ່ເຕັມ.')
            elif data == 5:
                stack.clear()
                print('Stack cleared.')
            elif data == 6:
                break
        else:
             print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງn")

