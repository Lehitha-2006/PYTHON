tuple=(1,2,3,4,5)
print(tuple)
print(type(tuple))

t=()
print(type(t)) #class tuple

print(len(tuple))

t=(10) # It is empty
print(type(t))
print(tuple[1])

t=(10,)
print(type(t))
#It will take this as element


#Accessing elements of tuple
t=(10,20,30,20,50,60)
print(t[2:5])  # range is from 2 to (n-1) so upto 4.
print(t[2:100]) #it is outo df index so it will print all the elements from index 2.
print(t[::2])  #Increment 2.


t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)

t1=t1*3
print(t1)

print(t1.count(10)) #In t1 the count of 10 & it is 3 times (t1*3)
print(sorted(t2))   #It will sort in ascending order


t=eval(input("Enter Tuple Of Number:"))
l=len(t)
sum=0
for x in t:  #For each element in t
      sum=sum+x
print("The Sum=",sum)
print("The Average=",sum/l)

t=[10,20,30,40,10,20,10]
s=set(t) #A set is a collection of unique elements — it automatically removes duplicates.
#The elements in a set are unordered, so the order may not match the original list.
print(s)
s=set(range(5)) ## s is now replaced → s = {0, 1, 2, 3, 4}
             # Output: {0, 1, 2, 3, 4}
print(s)


s = set(t)            # s = {10, 20, 30, 40}
s.update(range(5))    # adds 0 to 4 into s
print(s)              # Output: {0, 1, 2, 3, 4, 10, 20, 30, 40}

x=[4,3,2,1]  #List,not tuple
print(x)     #output:[4,3,2,1]
print(x.pop()) #output:1 (Removes and returns the last item)
print(x)       #output: [4,3,2]

x={1,2,3,4,5}
y={2,3,6,7,8}
print(x.union(y))  #Print all the elements

print(x.difference(y))
print(x-y)
print(x-y)

print(x.intersection(y)) #Print the common elements

print(x.symmetric_difference(y))
print(x^y)

s={x*x for x in range(5)}
print(s)






t=(10,20,30,40)
t[1]=70  #TypeError

print(tuple[100])  #Out of index So it will show error
