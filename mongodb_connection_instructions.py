import pymongo #import module
myclient=pymongo.MongoClient("mongodb://localhost:27017")#db connection
myclient.list_database_names()# print database names
['admin', 'config', 'local']
mydb=myclient["mydatabase"]#database creation
mycol=mydb["student"]# table creation
stud1={"name":"pratik mhaske","address":"pune"}#insert record
mycol.insert_one(stud1)#insert one record into db
<pymongo.results.InsertOneResult object at 0x000002ABCD764370>
print(mycol.find_one())#print one record
{'_id': ObjectId('62df75dbd79a2eff04a7d5a7'), 'name': 'pratik mhaske', 'address': 'pune'}
StudList=[{"name":"sachin chaudhari","address":"samrud"},
         {"name":"dhaval chaudhari","address":"bhusawal"},
         {"name":"nikhil nikam","address":"malegaon"}]# insert multiple records
mycol.insert_many(StudList)# insert multiple records into collection
for doc in mycol.find():#print all docs
      print(doc)

mydb.list_collection_names()#see the collections from db
StudList=[{"_id":1,"name":"arpit singh","address":"thane"},
         {"_id":2,"name":"hrutik ombale","address":"satara"},
         {"_id":3,"name":"hr","address":"satara"},
         {"_id":4,"name":"sachin chaudhari","address":"samrud"},
         {"_id":5,"name":"dhaval chaudhari","address":"bhusawal"},
         {"_id":6,"name":"nikhil nikam","address":"malegaon"}]#user defined id
mycol.insert_many(StudList)

for doc in mycol.find({},{"address":0}):#skip address and print remaining
      print(doc)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#writing queries in mongo db
myquery={"address":"satara"}#this will print only address==satara
for doc in mycol.find(myquery):
    print(doc)

aquery={"address":{"%gt":"s"}}#this will print only address name starting with s and s,t,u....z 
for doc in mycol.find(aquery):
    print(doc)
aquery={"address":{"$regex":"^s"}}#this will print only address name starting with s 
for doc in mycol.find(aquery):
    print(doc)

for doc in mycol.find().sort("name"):#print the records in ascending order
                    print(doc)

for doc in mycol.find().sort("name",-1):#print the records in descending order
                    print(doc)

myquery={"address":"satara"}#update one record
new_val={"$set":{"address":"satara,kedambe"}}
mycol.update_one(myquery,new_val)
for doc in mycol.find():
         print(doc)

myquery={"address":"satara"}#delete one record
mycol.delete_one(myquery)
<pymongo.results.DeleteResult object at 0x0000024AD5CC0E50>
for doc in mycol.find():
         print(doc)
