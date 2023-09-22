class CustomException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return(repr(self.msg))

try:
    age=int(input("Enter your age: "))
    if age>18:
        print("You can vote")
    else:
        raise CustomException("you can't vote")
    
except CustomException as e:
    print("A Custom/User defined Exception",e.msg)
