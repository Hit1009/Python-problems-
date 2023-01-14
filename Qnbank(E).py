#E1Compute Exponentiation (power of a number) without using ** operator.
n=int(input("Enter a number"))
p=int(input("Enter power"))
count=1
t=n
while count<p:
    t=t*n
    count+=1
print(n,"^",p,"=",t)

print("")

#E2Write a program in python to print all the two digit numbers which are either divisible by 3 or by 4.
n=10
print("All the two digit numbers which are either divisible by 3 or by 4 are:")
while n<100:
    if n%3==0 or n%4==0:
        print(n)
    n+=1
    
print("")

#E3Write a program in python to print the sum of all the digits of a number.
n=int(input("Enter a number:"))
t=n
sum=0
while t!=0:
    q=t%10
    sum+=q
    t=t//10
print("sum of digits =",sum)
 
print("")

#E4Perform the division operation and find the quotient and remainder values (without using /, // % operators)
dvd=int(input("Enter divident:"))
dvsr=int(input("Enter divisor:"))
t=dvd
q=0
while t-dvsr>=0:
    t=t-dvsr
    q+=1
rem=dvd-dvsr*q
print("quotient =",q,"remainder =",rem)

print("")

#E5Check whether the given number is palindrome or not
num = input('Enter any number : ')
val = int(num)
while num == str(num)[::-1]:
  print('The given number is PALINDROME')
  break
else:
  print('The given number is NOT a palindrome')

print("")

#E6Check whether the given number is Armstrong number or not
n=int(input("Enter a number"))
t=n
sum=0
p=len(str(n))
while t!=0:
    d=t%10
    sum=sum+d**p
    t=t//10
while n==sum:
    print(n,"is an Armstrong number")
    break
else:
    print(n,"is NOT an Armstrong number")    
    
print("")

#E7Compute the GCD of two numbers.(Euclidean Method and using common factors)
a=int(input("Enter greater number"))
b=int(input("Enter smaller number"))
t=a
while b!=0:
    a=b 
    b=t%b
    t=a
print("GCD is",a)

print("")

#E8Take integer inputs from user until he/she presses q Ask to press q to quit after every integer input Print average and product of all numbers
n=0
sum=0
p=1
count=0
while n!="q":
    n=input("Enter a number or press q to quit")
    if n!="q":
        sum=sum+int(n)
        count=count+1
        p=p*int(n)
avg=sum/count
print("Average=",avg," Product=",p)

print("")

#E9Find the square root of a number. (Newton’s method)
n=int(input("Enter a number"))
a=n/2
b=0
while b!=a:
    b=0.5*(a+n/a)
    a=b
print("sqrt",n,"=",a)


