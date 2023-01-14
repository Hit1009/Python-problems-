#C1Add, subtract, multiply and divide two integers by getting inputs from the user.
n1=int(input("Enter 1st number n1:"))
n2=int(input("Enter 2nd number n2:"))
sum=n1+n2
print("n1 + n2 =",sum)
diff=n1-n2
print("n1 - n2 =",diff)
p=n1*n2
print("n1 x n2 =",p)
d=n1/n2
print("n1/n2 =",d)
    
print("")  

#C2Swap the values of two variables using a temporary variable and multiple assignment.
a=int(input("a="))
b=int(input("b="))
c=a
a=b
b=c
print("a =",a,"b =",b)

print("") 
 
#C3Read the marks for five subjects and compute the total and average.
n1=int(input("Enter 1st subject marks:"))
n2=int(input("Enter 2nd subject marks:"))
n3=int(input("Enter 3rd subject marks:"))
n4=int(input("Enter 4th subject marks:"))
n5=int(input("Enter 5th subject marks:"))
tot=n1+n2+n3+n4+n5
print("Total marks =",tot)
print("Average marks =",tot/5)

print("") 
 
 #C4Find the area of rectangle, triangle and circle by reading inputs from the user.
l=float(input("Enter length of rectangle:"))
w=float(input("Enter width of rectangle:"))
b=float(input("Enter base of triangle:"))
h=float(input("Enter height of triangle:"))
r=float(input("Enter radius of circle"))
print("Area of rectangle =",l*w)
print("Area of triangle =",(1/2)*b*h)
print("Area of circle =",3.14*(r**2))

print("")

#C5Compute the square root of a given input number.
n=float(input())
sqrt=n**(1/2)
print("square root=",sqrt)

print("")

#C6Calculate Simple Interest.
p=int(input("Enter the principle amount:"))
t=int(input("Enter time duration:"))
r=int(input("Enter rate of interest:"))
s=(p*t*r)/100
print("simple interest=",s)

print("")

#C7 Find the net salary of an employee by getting the basic pay (BP) as input. 
bp=float(input("Enter your basic salary:"))
da=(88/100)*bp
hra=(8/100)*bp
cca=1000
insurance=2000
pf=(10/100)*bp
gpay=bp+da+hra+cca
ded=insurance+pf
netp=gpay=ded
print("net salary =",netp