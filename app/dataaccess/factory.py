from app.dataaccess.mongo_collections import PurchaseCollection, ResellerCollection
from app.dataaccess.rest_apis import CashBackAPI

#This is a layer of abstraction between services and data access objects
#this way it is possible to change how data is fetch without change service modules
class DataFactory():
  def add_purchase(self, purchase):
    return PurchaseCollection().add(purchase)
  
  def find_purchases_month(self, key, month, year):
    return PurchaseCollection().find_all_current_month(key, month, year)

  def add_reseller(self, reseller):
    return ResellerCollection().add(reseller)
  
  def find_reseller(self, key):
    return ResellerCollection().find_one(key)

  def get_cashback_amount(self, key):
    return CashBackAPI().get_cashback_amount(key)


    