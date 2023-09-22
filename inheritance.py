# class Employee:
#     def showDetails(self):
#         print("this is employee")
# class Programmer:
#     def showDetails(self):
#         print("this is programmer")
# class language(Programmer,Employee):
#     def showDetailss(self):
#         print("this is language")
# # e=Employee()
# # e.showDetails()
# # p=Programmer()
# # p.showDetails()
# l=language()
# # l.showDetail()
# l.showDetails()




class Employee:
    def showDetails(self):
        print("this is employee")
class Programmer:
    def showDetails(self):
        print("this is programmer")
class language(Employee,Programmer):
    def showDetailss(self):
        super().showDetails()
        print("this is language")
# e=Employee()
# e.showDetails()
# p=Programmer()
# p.showDetails()
l=language()
# l.showDetail()
l.showDetailss()

