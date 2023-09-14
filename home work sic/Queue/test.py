from queue import Queue

class CustomQueue:
    def __init__(self):
        self.items = Queue(maxsize=10)
    
    def push(self, item):
        if not self.is_full():
            print(f"ເພີ່ມ {item} ເຂົ້າ queue ສຳເລັດແລ້ວ")
            self.items.put(item)
        else:
            print('queue ເຕັມແລ້ວ!')

    def pop(self):
        if not self.is_empty():
            item = self.items.get()
            print(f"ນຳເອົາ {item} ອອກຈາກ queue ສຳເລັດແລ້ວ")
            return item
        else:
            print('queue ວ່າງ!')

    def is_full(self):
        return self.items.full()

    def is_empty(self):
        return self.items.empty()

    def clear(self):
        with self.items.mutex:
            self.items.queue.clear()

queue = CustomQueue()

while True:
    print('\n')
    print('=========================')
    print('       queue Management Menu       ')
    print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ queue: ')
    print('2.ດຶງຂໍ້ມູນອອກ queue:')
    print('3.ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ queue:')
    print('4.ກວດສອບ queue ວ່າເຕັມຫຼືບໍ່: ')
    print('5.Clear queue')
    print('6.ອອກຈາກໂປຣແກຣມ')
    choice = int(input('ເລືອກສິ່ງທີເຈົ້າຕ້ອງການ: '))
    if choice in (1,2,3,4,5,6):
        if choice == 1:
            item = input('ເພີ່ມຂໍ້ມູນເຂົ້າ queue: ')
            queue.push(item)
        elif choice == 2:
            item = queue.pop()
            if item is not None:
                print(f"ລຶບ {item} ແລ້ວ")
        elif choice == 3:
            print('queue= ', list(queue.items.queue))
        elif choice == 4:
            if queue.is_full():
                print('queue ເຕັມແລ້ວ')
            else:
                print('queue ຍັງບໍ່ເຕັມ.')
        elif choice == 5:
            queue.clear()
            print('queue cleared.')
        elif choice == 6:
            break
    else:
        print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງ")

