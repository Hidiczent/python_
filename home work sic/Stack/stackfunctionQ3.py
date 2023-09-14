from queue import LifoQueue
class Stack:
    def __init__(self):
        self.items=LifoQueue(maxsize=10)
    def push(self,item):
        if not self.is_full():
            print(f" ເພິ່ມ {item} ເຂົ້າ Stack ສຳເລັດແລ້ວ")
            self.items.put(item)
        else:
            print('Stack ເຕັມແລ້ວ! ')
    def pop(self):
        if not self.is_empty():
            print(f" ນຳເອົາ {item} ອອກຈາກ Stackສຳເລັດແລ້ວ ")
            return self.items.get()
        else:
            print('Stack ວ່າງ!')

    def is_full(self):
        return self.items.full()
    
    def is_empty(self):
        return self.items.empty()
    
    def clear(self):
        with self.items.mutex:
             self.items.queue.clear()
 
LIFO = Stack()

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
        choie=int(input('ເລືອກສິ່ງທີເຈົ້າຕ້ອງການ:'))
        if choie in (1,2,3,4,5,6):
            if choie == 1:
                item=input('ເພິ່ມຂໍ້ມູນເຂົ້າStack :')
                LIFO.push(item)
            elif choie == 2:
                LIFO.pop()
            elif choie == 3:
                print('Stack= ' , list(LIFO.items.queue))
            elif choie == 4 :
                if LIFO.is_full():
                     print('Stackເຕັມແລ້ວ')
                else:
                     print('Stackຍັງບໍ່ເຕັມ.')
            elif choie == 5:
                LIFO.clear()
                print('Stack cleared.')
            elif choie == 6:
                break
        else:
            print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງn")