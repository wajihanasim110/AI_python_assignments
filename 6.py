# get the volume of a sphere
a=input("Do you wish to enter radius or diameter?")
b=float(input("What is the radius or diameter?"))
pi=3.142
if a=="radius":
    c = ((4/3)*pi*b*b*b)
    print("The radius of the sphere is ",b)
    print(" The volume of the sphere is ", c)
else:
    d=b/2
    c = ((4/3)*pi*c*c*c)
    print("The radius of the circle is ",d)
    print(" The volume of the circle is ", c)