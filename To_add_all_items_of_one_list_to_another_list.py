x=[1,2,3,4,5]
order1=["Chicken","Mutton","Fish"]
order2=["RC","KF","PO"]
print(order1)


order1.extend("Mushroom")
print(order1)
#if u try to add string using "extend function" it stores each
#element in a string
x.remove(2)
print(x)
#if there are multiple occurances in the list the first occurance element will
#be removed using "remove function".
n1=[10,20,30]
print(n1.pop()) #the top most element will be removed and displyed same as stack
print(n1)

n1.reverse() #it is used to reverse the elements in the list
print(n1)


