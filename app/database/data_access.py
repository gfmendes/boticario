from app.database.db_config import database

class PurchaseDao():
  def add(self, purchase):     
    database.purchase.insert_one(purchase)
    return purchase

  def findAll(self, key):     
    return list(database.purchase.find(key))
        
class ResellerDao():
  def add(self, reseller):     
    database.reseller.insert_one(reseller)
    return reseller
    
  def findOne(self, key):     
    return database.reseller.find_one(key)
