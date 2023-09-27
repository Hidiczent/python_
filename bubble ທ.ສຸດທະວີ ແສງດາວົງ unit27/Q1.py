
def bubblesort(data):
    n=len(data)
    for i in range(n):
        print(data)
        for j in range(n-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]

s=[50,30,40,10,20]
bubblesort(s)
print(s)

#  ຈຳນວນທີ Swap ແມ່ນ 6 ຮອບ