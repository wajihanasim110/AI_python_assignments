#To calculate area of a circle
a=input("Do you wish to enter radius or diameter?")
b=float(input("What is the radius or diameter?"))
pi=3.142
if a=="radius":
    c = pi * b * b
    print("The radius of the circle is ",b)
    print(" The area of the circle is ", c)
else:
    d=b/2
    c = pi * d * d
    print("The radius of the circle is ",d)
    print(" The area of the circle is ", c)