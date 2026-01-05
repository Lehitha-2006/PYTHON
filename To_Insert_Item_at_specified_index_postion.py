x=[1,2,3,4,5]
x.insert(1,888)
print(x)

n=[1,2,3,4,5]
n.insert(10,777)
n.insert(-3,999)
print(n) #if the index is greater than the list then it is inserted
#at the end of the list
#(10,777)-here 10is the index no ,but in the given list there is no 10th
#index so it is inserted in the end.
#here the 777 is inserted at the end of the list and the index starts from
#left side and zero.
#(-3,999) - same as above but it is negative so index's starts from right side
#and starts from one.
