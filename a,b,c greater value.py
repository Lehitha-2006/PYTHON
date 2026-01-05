#ex-write a program to find biggest of given 3 numbers from the command prompt
a=int(input("enter the a value"))
b=int(input("enter the b value"))
c=int(input("enter the c value"))
if((a>b)and(a>c)):
 print("a is greater")
elif((b>a)and(b>c)):
 print("b is greater")
else:
 print("c is greater")
