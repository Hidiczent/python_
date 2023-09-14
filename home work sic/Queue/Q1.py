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
                if len(queue)==5:
                      print('quque')
                else:
                  item=int(input('ປ້ອນຂໍ້ມູນລົງໃນ quque : '))
                  print(f" ເພິ່ມ {item} ເຂົ້າ Stack ສຳເລັດແລ້ວ")
                  queue.append(item)
            #     
          elif (choice == 2):
                  item=queue[0]
                  print(f" ນຳເອົາ {item} ອອກຈາກ Stackສຳເລັດແລ້ວ ",queue.pop(0))
          elif (choice ==3 ):
               print('Queue = ',queue)
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


        