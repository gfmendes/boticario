import pymongo

client = pymongo.MongoClient("mongodb+srv://gmendes:Q1w2e3r4!@cluster0-zmuno.mongodb.net/boticario?retryWrites=true&w=majority")
database = client.boticario
collection = database.reseller

class ResellerDao():

  def add(self, reseller):     
    collection.insert_one(reseller)
    return reseller
    
  def find(self, key):     
    return collection.find_one(key)
        
