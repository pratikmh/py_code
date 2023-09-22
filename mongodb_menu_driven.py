import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myclient["mydatabase"]
mycol=mydb["student"]
  
  
def add():  
    StudList=[{"_id":1,"Student_name":"pratik mhaske","Course":"MCA"},
         {"_id":2,"Student_name":"sachin chaudhari","Course":"MBA"},
         {"_id":3,"Student_name":"hr ombale","Course":"MCA"},
         {"_id":4,"Student_name":"nikhil nikam","Course":"MBA"},
         {"_id":5,"Student_name":"saurav narkhede","Course":"BCA"},
         {"_id":6,"Student_name":"ganu gore","Course":"BBA"}]
    mycol.insert_many(StudList)
  
def display():  
    for doc in mycol.find():
      print(doc)  
  
def update():  
    myquery={"Course":"BBA"}
    new_val={"$set":{"Course":"BCS"}}
    mycol.update_one(myquery,new_val)
  
def delete():  
    myquery={"Course":"BCA"}
    mycol.delete_one(myquery) 
  
 
while True:  
    print("\nMAIN MENU")  
    print("1. add")  
    print("2. display")  
    print("3. update")
    print("4. delete")
    print("5. exit")
    choice = int(input("Enter the Choice:"))  
  
    if choice == 1:
         add()
         print("successfully added")

      
    elif choice == 2:
        display()

        
    elif choice == 3:
        update()
        print("Updation successfull")


    elif choice == 4:
        delete()
        print("Deletion successfull")

        
    elif choice == 5:  
        break  
      
    else:  
        print("Incorrect Choice.")  
