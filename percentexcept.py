class CustomException(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return(repr(self.msg))

try:
    percent=int(input("Enter your Percent:-"))
    if percent > 85 and percent < 100:
        print("Distinction")
    elif percent > 75 and percent < 100:
        print("First Class")
    elif percent > 55 and percent < 100:
        print("Second Class")
    elif percent > 35 and percent < 100:
        print("Third Class")
    else:
        raise CustomException ("failed")

except CustomException as e:
    print("You have been",e.msg)
