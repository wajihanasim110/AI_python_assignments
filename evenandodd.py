def even_odd(num):
    if num%2==0:
        a=0
        return a
    else:
        a=1
        return a
num=int(input("enter a random number"))
ans = even_odd(num)
if ans == 0:
    print(num," is even  number")
else:
    print(num," is odd number")