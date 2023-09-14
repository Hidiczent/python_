def push(queue,item):
        if len(queue) == 5:
                print ('Queue ເຕັມແລ້ວ')
        else:
            queue.append(item)
def pop(queue):
    if len(queue) == 0:
              print('Queue is empty')
    else:
        item=queue[0]
        print(f"ນຳເອົາ{item} ອອກຈາກ queue ສຳເລັດແລ້ວ")

def display(item):
      if len(queue) == 0:
        print('Queue is empty')
      else:
            print('Queue ປະກອບມີ')
            for item in reversed(queue):
                  print(item)

def clear(self):
      self.queue.clear()
queue=[]
while True:
    print('\n')
    print('=========================')
    print(' ຈັດການໂຄງການ Stack ')
    print('1.ເພີ່ມຂໍ້ມູນເຂົ້າ Stack: ')
    print('2.ເອົາຂໍ້ມູນອອກ Stack:')
    print('3.ສະແດງຄ່າຂໍ້ມູນທີ່ເກັບໃນ Stack: ')
    print('4.ອອກຈາກໂປຣແກຣມ: ')
    print("========================")
    choice = int(input("Enter the choice:"))
    if  choice in  (1,2,3,4,5,6):
          if (choice==1):
                item=int(input('ປ້ອນຂໍ້ມູນລົງໃນ quque : '))
                push(queue,item)
          elif (choice == 2):
                pop(queue)
          elif (choice ==3 ):
                display(item)
          elif (choice ==4):
                    if len(queue)==0:
                        print('queue ເຕັມແລ້ວ')
                    else:
                          print('queue ຍັງບໍ່ເຕັມ')
                # print('queue cleared.')
          elif (choice == 5):
                queue.clear()
                print('queue cleared.')
          elif (choice == 6):
                break
    else:
         print("ທາງເລືອກບໍ່ຖືກຕ້ອງ, ກະລຸນາລອງໃໝ່ອີກຄັ້ງ")


        