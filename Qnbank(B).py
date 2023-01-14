#B1Given age determine whether a person is eligible to vote or not. (if else)
age=int(input("Enter your age:"))
if age>=18:
    print("congratulations you are eligible to vote")
else:
    print("sorry you are not eligible to vote")
    
print("")

#B2Check whether a number is odd or even.
n=int(input("Enter a number:"))
if n%2==0:
    print(n,"is an even number")
else:
    print(n,"is an odd number")
    
print("")

#B3Write a program to find largest of two numbers
n1=float(input("Enter 1st number:"))
n2=float(input("Enter 2nd number:"))
if n1>n2:
    print(n1,"is largest")
else:
    print(n2,"is largest")
    
print("")

#B4Obtain a character convert lower case to uppercase and vice versa. 
a=input("Enter a lower case character:")
if a.upper()!=a:
    print(a.upper())
else:
    print(a.lower())

print("")

#B5Find the input year is leap year or not.
y=int(input("Enter a year:"))
if y%4!=0:
    print(y,"is not a leap year")
else:
    if y%100!=0:
        print(y,"is a leap year")
    else:
        if y%400!=0:
            print(y,"is not a leap year")
        else:
            print(y,"is a leap year")
             
print('')

#B6Read a number, check if it is positive, negative or zero. Increment the number if it is positive, decrement if it is negative. 
n=float(input("Enter a number:"))
if n<0:
    print(n,"is negative","decrement=",n-1)
elif n==0:
    print(n,"is zero")
elif n>0:
    print(n,"is positive, increment=",n+1)
  
print("")  

#B7Create a simple calculator
print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
a=int(input("Enter 1,2,3 or 4:"))
n1=float(input("Enter 1st number n1:"))
n2=float(input("Enter 2nd number n2:"))
if a==1:
    sum=n1+n2
    print("n1 + n2 =",sum)
elif a==2:
    diff=n1-n2
    print("n1 - n2 =",diff)
elif a==3:
    p=n1*n2
    print("n1 x n2 =",p)
elif a==4:
    d=n1/n2
    print("n1/n2 =",d)
    
print("")   
 
#B8Estimate the Grade based on the marks obtained by a student.    
print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")

print("")

#B9Find the largest of 3 numbers. 
n1=float(input("Enter 1st number n1:"))
n2=float(input("Enter 2nd number n2:"))
n3=float(input("Enter 3rd number n3:"))
if n1>n2 and n1>n3:
    print(n1,"is largest")
elif n2>n1 and n2>n3:
    print(n2,"is largest")
elif n3>n1 and n3>n2:
    print(n3,"is largest") 

print("")

#B10 Obtain a character, check if it is lower case, uppercase or digit
n = input("Enter a character:  ")
if n <=str(9) and len(n)==1:
    print(n,"is digit")
elif len(n)!=1:
    print("Error, enter 1 digit character")
else:
    if n==n.upper():
        print(n,'is uppercase')
    else:
        print(n,'is lowercase'