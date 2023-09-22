class student:
    def __init__(self,rollno,name,m1,m2):
        self.m1=m1
        self.m2=m2
        self.name=name
        self.rollno=rollno

    def display(self):
        print("rollno",self.rollno)
        print("name",self.name)
        print("marks of subject 1:",self.m1)
        print("marks of subject 2:",self.m2)
        print(self.grace_marks)

def result(self):
    print("rollno",self.rollno)
    print("percentage=",(self.m1+self.m2+grace_marks)/3)

grace_marks=10
s1=student(101,"pratik",80,70)
s1.grace_marks=grace_marks
s1.display()
print(s1.grace_marks)
