#I1.Define a function to count the number of occurrences of a substring in a given string and print the starting index of the substring for each occurrence. 
def substr(a):
    global string
    b=len(a)
    count=0
    for i in range(len(string)):
        if string[i:(b+i)]==a:
           count+=1
           print(a,"starts at index",i)
    return count
string="go mango go"
a="go"
print("substring",a,"occurs",substr(a),"times in",string)

print()

#I2.Encrypt a given message by “rotating” each letter by a fixed number of places
def rotate_word(word,rot):
    alp=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    a=""
    for i in word:
        if i in alp:
            i=alp[alp.index(i)+rot]
            a+=i
    return a
print(rotate_word("HAL",2))

print()

#I3.Write a user-defined function to check whether a given text is palindrome or not using string slice method.
def palchk(a):
    b=""
    for i in range(len(a)):
        b+=a[-1-i]
    if b==a:
        return "palindrome"
    else:
        return "Not a palindrome"
print(palchk("malayalam"))
print(palchk("tamil"))

print()

#I4.Write a function strip_characters(str,chars) which removes the characters mentioned in chars from the string str.
def strip_characters(str,chars):
    charlist=[]
    strlist=[]
    for i in chars:
        charlist.append(i)
    for i in str:
        strlist.append(i)
    for i in charlist:
        for j in strlist:
            if i==j:
                strlist.remove(i)
    newstr=""
    for i in strlist:
        newstr+=i
    return newstr      
print(strip_characters("The quick brom fox jumps over the lazy dog","aeiou"))