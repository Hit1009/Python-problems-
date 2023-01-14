#G1. Write a user-defined function to read the marks of 5 subjects, compute the total marks scored,average, and grade of the student. The function should take the name and ID of the student asarguments and print student name, ID, total, average, and grade. Write a Python program to print the mark details for N students using the function. 
def marks_report(student):
    total_mks=calculus+chemistry+eee+python+softskills
    avg_mks=total_mks/5
    print("Name:",student["name"])
    print("ID:",student["id"])
    print("Total Marks=",total_mks)
    print("Average Marks=",avg_mks)
    if avg_mks>=45:
        print("S Grade")
    elif avg_mks>=40 and avg_mks<45:
        print("A Grade")
    elif avg_mks>=35 and avg_mks<40:
        print("B Grade")
    elif avg_mks>=30 and avg_mks<35:
        print("C Grade")
    elif avg_mks>=25 and avg_mks<30:
        print("D Grade")
    elif avg_mks>=20 and avg_mks<25:
        print("E Grade")
    elif avg_mks<20:
        print("F Grade")
calculus=44
chemistry=38
eee=45
python=40
softskills=45
marks_report({"name":"Hitarth Vyas","id":"22BRS1328"})

print()

#G2. Write a function power(X,N) that will allow a floating-point number to be raised to an integerpower and return the result. i.e. Y = X N. Write a Python program to invoke the function
def power(X,N):
    p=X**N
    return p
print(power(6.9,5))

print()

#G3.Define a function CheckOddEven(num) that checks if the num is odd or even; the function sets a flag accordingly and returns it. Use this function to find the sum of even and odd numbers separately, from a given input of N numbers.
def CheckOddEven(num):
    if num%2==00:
        global evensum
        evensum+=num
        return "Even"
    else:        
        global oddsum
        oddsum+=num
        return "Odd"
evensum=0
oddsum=0
N=3 #Number of inputs given
for i in range(N):
    a=int(input())
    print(CheckOddEven(a))
print("EvenSum =",evensum,"OddSum =",oddsum)

print()

#G4. Define a function to find the factors of the given number as an argument. If the number is not given, then display the factors of the default argument.
def factors(n=5):
    print("factors of",n,"are",end=" ")
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=",")
factors(10) #defining an argument
print()
factors() #function taking default argument i.e 5

print("\n")

#G5. Modify the function in Qn. (1) so that it returns total marks, average and grade of a student.
def marks_report(student):
    def ttlmks():
        global total_mks
        total_mks=calculus+chemistry+eee+python+softskills
        return total_mks
    print("Total Marks =",ttlmks())
    def avgmks():
        global avg_mks
        avg_mks=total_mks/5
        return avg_mks
    print("Average Marks =",avgmks())
    def grd():
        global avg_mks
        if avg_mks>=45:
            return "S Grade"
        elif avg_mks>=40 and avg_mks<45:
            return "A Grade"
        elif avg_mks>=35 and avg_mks<40:
            return "B Grade"
        elif avg_mks>=30 and avg_mks<35:
            return "C Grade"
        elif avg_mks>=25 and avg_mks<30:
            return "D Grade"
        elif avg_mks>=20 and avg_mks<25:
            return "E Grade"
        elif avg_mks<20:
            return "F Grade"
    print(grd())
calculus=44
chemistry=38
eee=45
python=40
softskills=45
marks_report({"name":"Hitarth Vyas","id":"22BRS1328"})