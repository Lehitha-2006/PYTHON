class parent:
    def show(self):
        print("parent")
class child1(parent):
    pass
class child2(parent):
    pass
c1=child1()
c2=child2()
c1.show()
c2.show()
