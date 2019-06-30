#to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
number=int(input("please enter a number to check whether it's even or odd"))
if number%2 == 0:
    print("number "+ str(number)+"is even")
else:
    print("number "+str(number)+"is odd")