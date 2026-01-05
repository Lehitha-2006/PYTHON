class Animal:  
     def make_sound(self):  
          print("Some sound")  
class Dog(Animal):  
     def make_sound(self):  
          print("Bark")  
class Cat(Animal):  
     def make_sound(self):  
          print("Meow")  
class Bird(Animal):  
    def make_sound(self):  
         print("Chirp")  
animals=[Dog(),Cat(),Bird()]  
for animal in animals:  
    animal.make_sound()  

################################################

import numpy as np  

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Add:", np.add(a, b))
print("All non-zero:", np.all(a))
print("Greater:", np.greater(b, a))
print("Greater equal:", np.greater_equal(b, a))
print("Less:", np.less(a, b))
print("Less equal:", np.less_equal(a, b))
print("Equal:", np.equal(a, b))
print("All close:", np.allclose(a, [1, 2, 3]))
print("Zeros:", np.zeros(3))
print("Ones:", np.ones(3))
print("Linspace:", np.linspace(0, 1, 5))
print("To list:", a.tolist())

###############################################


import numpy as np  
arr=np.array([1,3,2,3,4,2,1,5])  
print("Max:",np.max(arr))  
print("Min:",np.min(arr))  
print("Argmax:",np.argmax(arr))  
print("Argmin:",np.argmin(arr))  
print("Unique:",np.unique(arr))  
print("Bincount:",np.bincount(arr))
print("repr:",repr(arr))
import numpy as np

arr = np.array([1, 3, 2, 3, 4, 2, 1, 5])

counts = np.bincount(arr)  # Count of all integers from 0 to max(arr)

for i in range(1, len(counts)):  # Start from 1 since 0 is not in arr
    print(f"Count of {i}:", counts[i])
