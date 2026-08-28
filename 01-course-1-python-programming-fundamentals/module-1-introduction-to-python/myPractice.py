print("Chal Baar")
input= "lovely"
inl="4"
print(type(input))
print(ord(inl))
#index: left to right start with 0
#index: right to left start with -1
print(input[1]) # print: o
print(input[-1]) # print: y
# slicing:
print(input[0:4:1])#0 index se start, 4 index pe stop, 1 ka increment. #  print: love 

#task:
word="hello how are you?"
print(word[0:5]) # print: hello
print(word[6:9]) # print: how

a=12
b=0
print((bool(a))) #first 7 values=false, then 8 and above values=true
print((bool(b))) 
a=float(a)#manual type casting
print(type(a))
c=a/12
print(type(c))
name=input("Enter your name: ") # input show on screen, datatype will be string 
# so if we want int input, type cast it to int
age=int(input("Enter your age: ")) # input show on screen, datatype will be string, type cast it to int
print("Enter your name:") # output show on screen
print(f"Your name: {name}") # formatted output 
#or
print("Your name: " + name) # concatenation
#or
print("Your name: ", name) # comma separated
#arithmetic operations:
#+,-,/,//,*,**,%
q=12
print(q/12) # print: 1.0, to get result in integer, use // operator
print(q//12) # print: 1
# or 
print(int(q/12)) # print: 1
print(q**2) # print: 144  power/exponential operator
#not follow bodmas rule, it will evaluate from left to right
#multiplication and division evaluated first, addition and subtraction after multiplication and division
#** right to left associativity, high precedence than multiplication and division, evaluated first, then multiplication and division, then addition and subtraction

#comparison operators:
#==,!=,>,<,>=,<=
print(5==5) # print: True
print(5!=5) # print: False

#logical operators:
#and, or, not

#assignment operators:
#=,+=,-=,*=,/=,//=,**=,%=

#compound operators:
#if, else, elif

year=int(input("Enter the year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")

temperature=int(input("Enter the temperature: "))
if temperature>30:
    print("It's a hot day")

#for loop:
for i in range(5): #range(start, stop, step)
    print(i) # print: 0,1,2,3,4

n=int(input("Enter the number: "))
for i in range(n, (n*10)+1, n): 
    print(i) # print: n, 2n, 3n, 4n, 5n, 6n, 7n, 8n, 9n, 10n
#or 
print(f"{n}*{i}={n*i}") # print: n*i=n*i

a="hello"
b=input("Enter a string: ")
for i in a:
    print(i) # print: h,e,l,l,o
for char in a:
    print(char) # print: h,e,l,l,o
for i in range(0,len(b)): # based on index
    print(f"{i}: {b[i]}") # print: each character of the string b
l=0
for i in range(1,n+1): #i=0 to n, run untill i!=n+1
    l=l+i   #
    print(l) # print: sum  till n

#factorial of a number:
factorial=1 
for i in range(1,n+1):
    factorial=factorial*i
    print(factorial) # print: factorial of n

#even sum:
even_sum=0
odd_sum=0
for i in range(1,n+1):
    if i%2==0:
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
print(even_sum) # print: sum of even numbers till n
#or
for i in range(2,n+1,2):
    even_sum=even_sum+i
print(even_sum) # print: sum of even numbers till n

#factors of a number:
for i in range(1,n+1):
    if n%i==0:
        print(i) # print: factors of n
    
#perfect number:
sum_of_factors=0
for i in range(1,n):
    if n%i==0:
        sum_of_factors=sum_of_factors+i
if sum_of_factors==n:
    print(f"{n} is a perfect number") # print: n is a perfect number
else:
        print(f"{n} is not a perfect number") # print: n is not a perfect number
    
factors=0
#prime number:
for i in range(1,n+1):
        if n%i==0:
            factors=factors+1
if factors==2:
        print(f"{n} is a prime number") # print: n is a prime number 
else:
        print(f"{n} is not a prime number") # print: n is not a prime number   

#reverse of a string:
string=input("Enter a string: ")
reverse=""
for i in range(len(string)-1,-1,-1):
    reverse=reverse+string[i]
print(f"Reverse of {string} is {reverse}")
if string==reverse:
    print(f"{string} is a palindrome") # print: string is a palindrome
#or
print(string[::-1]) # print: reverse of string--string slicing

#count characters,digits,special characters in a string:
string=input("Enter a string: ")
characters=0
digits=0
sp_characters=0
for i in string:
    if i.isalpha():
        characters=characters+1
    elif i.isdigit():
        digits=digits+1
    else:
        sp_characters=sp_characters+1
print(f"Characters: {characters}")
print(f"Digits: {digits}")
print(f"Special Characters: {sp_characters}")
#or
for i in string:
    if i.ord()>=65 and i.ord()<=90 or i.ord()>=97 and i.ord()<=122:
        characters=characters+1
    elif i.ord()>=48 and i.ord()<=57:
        digits=digits+1
    else:        sp_characters=sp_characters+1
print(f"Characters: {characters}")
print(f"Digits: {digits}")
print(f"Special Characters: {sp_characters}")

#break and continue and else in loops:
for i in range(5):
    if i==3:
        break # it will exit the loop when i is 3
    print(i) # print: 0,1,2
else: 
    print("Loop ended without break") # it will not execute because of break statement
for i in range(5):
    if i==3:
        continue # it will skip the iteration when i is 3
    print(i) # print: 0,1,2,4
for i in range(n):
    print("Hello") # print: Hello n times

#while loop:
i=0
while i<n:
    print("Hello") # print: Hello n times
    i=i+1

infinite
p=0
while True:
    print (p) # print: 0,1,2,3,4,5,6,7,8,9,10...
    p=p+1

a=0
while a!=20:
    print(a) # print: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
    a=a+1
#print number into seperate digits:
n= 786
while n>0:
    digit=n%10
    print(digit) # print: each digit of the number n
    n=n//10
    #or
a=str(n)
print(a[0]) # print: 7
print(a[1]) # print: 8  
print(a[2]) # print: 6

n=int(input("Enter a number: "))
while n>0:
    print(n%10) # print: each digit of the number n
    n=n//10

n=int(input("Enter a number: "))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10 
    print(reverse) # print: reverse of the number n