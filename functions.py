#how to make a function
a=int(input("enter the first number"))
b=int(input ("enter the second number"))
def add(num1,num2):
    addition=num1+num2
    print("the sum of two numbers is:", addition)
add(a,b)

def multiply (no1,no2):
    product = no1 * no2
    print("the product of two numbers is:",product)
multiply(a,b)
def subtract(n1,n2):
    if n1 >= n2:
        subtraction = n1-n2
    else:
        subtraction = n2-n1
    print("the difference between two number is:", subtraction)
subtract(a,b)
def divide(a1,a2):
    if a1 >= a2:
        division = a1/a2
    else:
        division = a2/a1
    print("The division between the two number gives:", division)
divide(a,b)