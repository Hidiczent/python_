def insertionsort2(S):
    n = len(S)
    for i in range(1,n):
        print(S)
        x = S[i]
        j = i-1
        while j >= 0 and S[j] > x:
           S[j+1] =S[j]
           j-=1
           S[j+1] = x 
S=[50,30,40,10,20]
insertionsort2(S)
print(S)

#  ຈຳນວນທີ Swap ແມ່ນ 5 ຮອບ