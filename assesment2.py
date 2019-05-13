#To extract list of 1000 numbers and determine the minimum, maximum and mean value of the same
#Print List of 1000 random Numbers#
a=[]
import random
for m in range(1001):
        a.append(random.randint(1,1001))
b=a[0]
print("The list of random numbers is:")
print(a)
#Print Minimum Value from the list#
x=0
for n in range(len(a)):
   if b>a[n]:
       b=a[n]
       x=n
print("Minimum value from the above list is",b,", which is at",x,"index number")
#Print maximum value from the list#
for o in range(len(a)):
   if b<a[o]:
       b=a[o]
       x=o
print ("Maximum value from the above list is",b,", which is at",x,"index number")
#Print mean of the extracted random numbers
sum=0
for p in range(len(a)):
    sum=sum+a[p]
average=sum/len(a)
print("The mean of the random list is ",average)
#End of program#