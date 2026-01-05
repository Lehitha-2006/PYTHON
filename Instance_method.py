class student:
    def __int__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hi',self.name)
        print('Your Marks are:',self.marks)
    def grade(self):
        if self.amrks>=60:
            print('You got first grade')
        elif self.marks>=50:
            print('You got second grade')
        elif self.marks>=35:
            print('You got third grade')
        else:
            print('You are failed')
n=int(input('Enter number of students:'))
for i in range(n):
      name=input('Enter marks:')
      s=student(name,marks)
      s.display()
      s.grade()
      print()
