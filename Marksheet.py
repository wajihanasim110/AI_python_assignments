a=str(input("What is the student's name?"))
b=int(input("what is student's roll number?"))
c=str(input(" Enter 1st subject name"))
d=int(input("Enter 1st subject marks"))
e=str(input(" Enter 2nd subject name"))
f=int(input("Enter 2nd subject marks"))
g=str(input(" Enter 3rd subject name"))
h=int(input("Enter 3rd subject marks"))
i=str(input(" Enter 4rth subject name"))
j=int(input("Enter 4rth subject marks"))
k=str(input(" Enter 5th subject name"))
l=int(input("Enter 5th subject marks"))
print("Student Name:", a)
print("Student ID:", b)
if d>91 and d<100:
    print(c,d,": A+") 
elif d>81 and d<90:
    print(c,d,": A")
elif d>71 and d<80:
    print(c,d,": B+")
elif d>61 and d<70:
    print(c,d,": B")
elif d>56 and d<60:
    print(c,d,": C+")
elif d>51 and d<55:
    print(c,d,": C")
else:
    print(c,d,": D")
if f>91 and f<100:
    print(e,f,": A+") 
elif f>81 and f<90:
    print(e,f,": A")
elif f>71 and f<80:
    print(e,f,": B+")
elif f>61 and f<70:
    print(e,f,": B")
elif f>56 and f<60:
    print(e,f,": C+")
elif f>51 and f<55:
    print(e,f,": C")
else:
    print(e,f,": D")
if h>91 and h<100:
    print(g,h,": A+") 
elif h>81 and h<90:
    print(g,h,": A")
elif h>71 and h<80:
    print(g,h,": B+")
elif h>61 and h<70:
    print(g,h,": B")
elif h>56 and h<60:
    print(g,h,": C+")
elif h>51 and h<55:
    print(g,h,": C")
else:
    print(g,h,": D")
if j>91 and j<100:
    print(i,j,": A+") 
elif j>81 and j<90:
    print(i,j,": A")
elif j>71 and j<80:
    print(i,j,": B+")
elif j>61 and j<70:
    print(i,j,": B")
elif j>56 and j<60:
    print(c,d,": C+")
elif j>51 and j<55:
    print(i,j,": C")
else:
    print(i,j,": D")
if l>91 and l<100:
    print(k,l,": A+") 
elif l>81 and l<90:
    print(k,l,": A")
elif l>71 and l<80:
    print(k,l,": B+")
elif l>61 and l<70:
    print(k,l,": B")
elif l>56 and l<60:
    print(k,l,": C+")
elif l>51 and l<55:
    print(k,l,": C")
else:
    print(k,l,": D")
sum=d+f+h+j+l
print("Total Marks: ",sum,"/500")
per=sum/500*100
print("Percentage: ", per)
if sum>451 and sum<500:
    print("The overall grade is A+") 
elif sum>401 and sum<450:
    print("The overall grade is A")
elif sum>376 and sum<400:
    print("The overall grade is B+")
elif sum>351 and sum<375:
    print("The overall grade is B")
elif sum>301 and sum<350:
    print("The overall grade is C+")
elif sum>250 and d<300:
    print("The overall grade is C")
else:
    print("The overall grade is D. FAILED")