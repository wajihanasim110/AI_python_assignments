#to get the difference between a given number and 17, difference cannot be negative
a=int(input("Enter a number"))
b=17
c=a-b
if c < 0:
    print("The difference is negative.")
else:
    print(c)