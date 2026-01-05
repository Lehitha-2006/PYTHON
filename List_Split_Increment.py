list1=[10,'a',30,'d',50]
print(list1)
print(list1[0])

print(list1[1])

print(list1[2])

print(list1[3])

print(list1[4])

print(list1[-1])

print(list1[-2])

print(list1[-3])




print(list1[-5])


list1[1]='p'

print(list1[1])

print(type(list1))


list=[]

print(list)


list2=eval(input("ENTER LIST:"))

print(list2)

print(type(list2))




s="LEARNING PYTHON IS VERY EASY !!!"
I=s.split()
print(I)
print(type(I))

n=[1,2,3,4,5,6,7,8,9]
print(n[2:7:2])
print(n[0:2:1])
print(n[4::2]) #from 4 till the end with increment of 2
print(n[1:5])#from one till 5 automatically increment will be one till end

m=[1,2,3,4,5,6,7]
print(3 in n)# or for i in n:
            #   print(i)


n=[1,2,3]
i=0;
while i<len(n):
    print(n[i])
    i=i+1
