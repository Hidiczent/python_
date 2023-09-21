from random import randint

maximum = int(input("Enter the number of maximum : "))
number = int(input("Enter your guessing number : "))
count = 0 
low, high = 1, maximum

while low < high:
    mid = (low + high)//2
    count += 1
    if mid == number:
        print(f"Your number is {number}.")
        break
    elif mid > number:
        high = mid - 1
    else:
        low = mid + 1

print(f"Total  {count} times are searched. ")

#output :
    # Enter the number of maximum : 100
    # Enter your guessing number : 51
    # Your number is 51.
    # Total  6 times are searched.