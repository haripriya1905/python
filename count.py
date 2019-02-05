# Python Program to Count Number of Digits in a Number using While loop

Number = int(input(" Enter any Num: "))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1

print("\n Number of Digits in a Given Number = %d" %Count)
