from app.data.mongo_collections import ResellerCollection, PurchaseCollection
from app.data.rest_apis import CashBackAPI

#This module is a layer of abstraction between services and data access objects
#this way it is possible to change how data is fetch without change service modules
class PurchaseData():
  def add_purchase(self, purchase):
    return PurchaseCollection().add(purchase)
  
  def find_monthly_purchases(self, key):
    return PurchaseCollection().find_all_current_month(key)

class ResellerData():
  def add_reseller(self, reseller):
    return ResellerCollection().add(reseller)
  
  def find_reseller(self, key):
    return ResellerCollection().find_one(key)

class CashBackData():
  def get_cashback_amount(self, key):
    return CashBackAPI().get_cashback_amount(key)