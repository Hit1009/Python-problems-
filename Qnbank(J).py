#J1. Read a list of elements from the user and perform the following operations using functions: search(key): to find the given key in the list and display the position of the key if found, otherwise display appropriate message, maximum(Lst) and minimum(Lst) to find the maximum and minimum number respectively from the list. 
def search(key):
    global lst
    if key in lst:
        print("The index of key",key,"is",end=" ")
        return lst.index(key)
    if key not in lst:
        return "sorry key not found"
lst=[1,2,3,4,5,6]
print(search(6))
def  maximum(Lst):
    global lst
    return max(lst)
print("Maximum number is",maximum(lst))
def minimum(Lst):
    global lst
    return min(lst)
print("Minimum number is",minimum(lst))

print()

#J2.Two words are anagrams if you can rearrange the letters from one word to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams. 
def is_anagram(a,b):
    if sorted(a.lower())==sorted(b.lower()):
        return True
print(is_anagram("School master","The"))
print(is_anagram("classroom Listen","Silent"))
print(is_anagram("A gentleman","Elegant man"))

print()

#J3.Write a function sorted that takes a list as a parameter and sort the elements in lexicographical order. Test the function for a list of names and print the sorted list.
def sorted(names):
    string=""
    for i in  names:
        string+=i+" "
    b=string.split()
    b.sort()
    print(b)
sorted(["Ram","Shyam","Arjun","Riya","Rahul"])

#J4.A list of students registered for Python course. Perform the following operations (use inbuilt functions) and print the output:
students=["Ram","Shyam","Arjun","Riya","Rahul"]
newreg="Alok"
students.append(newreg) #adding new student
print(students)
print("Number of students registered for python are",len(students))
students[-2]="Rajesh" #Modifying a name in the list. 
print(students)
students.sort() #sorting name list
print(students)
newstud="Varun"
students.insert(2,newstud) #inserting newstudent at index 2
print(students)
if "Varun" in students: #searching for a student
    print("Varun","found!")
students.remove("Riya") #Removing a given name from a list
print(students)

print()

#J5.Consider a tuple as T = (1, 3, 2, 4, 6, 5). Write a program to store numbers present at odd index into a new tuple.
T=(1,3,2,4,6,5)
l=[]
for i in range(len(T)):
  if i%2==1:
    l.append(T[i])
newT=tuple(l)
print(newT)

print()

#J6.
n=int(input("Enter the number of food items in the menu: "))
food=[]
price=[]
amount=0
for i in range(1,n+1):
    a=input("Enter an item: ")
    n=int(input("Enter item's price per k.g: "))
    food.append(a)
    price.append(n)
    q=int(input("Enter the quantity of the item(in k.g: )"))
    amount+=q*n
print("Total amount =",amount)