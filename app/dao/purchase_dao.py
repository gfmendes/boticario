import pymongo

client = pymongo.MongoClient("mongodb+srv://gmendes:Q1w2e3r4!@cluster0-zmuno.mongodb.net/boticario?retryWrites=true&w=majority")
database = client.boticario
collection = database.purchase

class PurchaseDao():

  def add(self, purchase):     
    collection.insert_one(purchase)
    return purchase

  def find(self, key):     
    return list(collection.find(key))
        
