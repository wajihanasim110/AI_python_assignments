# to get a string which is n (non-negative integer) copies of a given string
a= input("enter a sentence you want to repeat")
b = int(input("Enter the repition value"))
if b <=0:
    print ("The repitition of", a ,"is not possible")
else:
    for i in range (b):
        print (a) 