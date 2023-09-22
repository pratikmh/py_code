import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myclient["mydatabase"]
mycol=mydb["student"]
  
  
def add():  
        student_id = input('Enter student id :')
        student_name = input('Enter Student Name :')
        course = input('Enter course :')

        mycol.insert_one({
                "student_id":student_id,
                "student_name":student_name,
                "course":course
                })
  
def display():  
    for doc in mycol.find():
      print(doc)  
  
def update():  
        criteria = input('\nEnter id to update\n')
        student_name = input('\nEnter Student Name :\n')
        course = input('\nEnter course :\n')
        mycol.update_one(
            {"student_id": criteria},
            {
                "$set": {
                "student_name":student_name,
                "course":course
                }
            }
        )
          
  
def delete():

        criteria = input('\nEnter student id to delete\n')
        mycol.delete_one({"student_id":criteria})

  
 
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
