class Faculty:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def marks(self):
        return self.m1+self.m2+self.m3
class Student:
    def __init__(self,rollno,name,m1,m2,m3):
                 self.rollno=rollno
                 self.name=name
                 self.obj_Faculty=Faculty(m1,m2,m3)
    def total_marks(self):
        print(self.obj_Faculty.marks())

s1=Student(101,"pratik",50,40,60)
s1.total_marks()
