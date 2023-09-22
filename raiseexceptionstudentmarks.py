class Customexception(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return(repr(self.msg))
try:
    roll=input("enter roll no")
    name=input("enter name")
    percent=int(input("enter percent"))
    if percent>60 and percent<100:
        print(roll,name,"first class")
    elif percent>50 and percent<60:
        print(roll,name,"second class")
    elif percent>35 and percent<50:
        print(roll,name,"third class")
    else:
     raise Customexception("you are fail")

except Customexception as e:
    print("A user exception found:-",e.msg)
 
