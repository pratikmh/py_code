class ClassMethod:
    def instanceMethod(self):
        print("instance method")
    @classmethod
    def ClassMethod(cls):
        print("class method")
ob=ClassMethod()
ob.instanceMethod()
ClassMethod.ClassMethod()
ob.ClassMethod()
