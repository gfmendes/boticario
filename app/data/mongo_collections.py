import json
import pymongo

client = pymongo.MongoClient("mongodb+srv://gmendes:Q1w2e3r4!@cluster0-zmuno.mongodb.net/boticario?retryWrites=true&w=majority")
database = client.boticario

class PurchaseCollection():
  def add(self, purchase):
    database.purchase.insert_one(purchase)
    return purchase

  def find_all_per_month(self, key):
    
    result = database.purchase.find(
      { "$and": [  
          {"$expr": { "$eq": [{ "$year": [{ "$dateFromString": { "dateString" : "$date" }}]}, key['year']]}},
          {"$expr": { "$eq": [{ "$month": [{ "$dateFromString": { "dateString" : "$date" }}]}, key['month']]}},
          { "cpf" : key['cpf']}
      ]}, {'_id': False})
    return list(result)

class ResellerCollection():
  def add(self, reseller):     
    database.reseller.insert_one(reseller)
    return reseller
    
  def find_one(self, key):     
    return database.reseller.find_one(key)
