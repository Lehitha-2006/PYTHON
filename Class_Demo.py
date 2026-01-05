class Student:
    def _init_(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def talk(self):
        print("Hello I am:", self.name)
        print("My Age is:", self.age)
        print("My Marks are:", self.marks)

s = Student('Lehitha',19,90)
s.talk()
