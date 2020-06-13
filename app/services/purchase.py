import logging
import datetime
from app.dataaccess.factory import DataFactory

PRE_APPROVED_RESELLERS = ['15350946056'] #This information should be externalized, for example in an API call or database

class PurchaseService():
  def add_purchase(self, purchase):
    logging.warn("Adding new purchase request %s" % purchase)
    purchase['status'] = 'Approved' if purchase['cpf'] in PRE_APPROVED_RESELLERS else 'Validating'
    purchase = DataFactory().add_purchase(purchase)
    return {"success": str(purchase)}

  def validate_purchase(self, purchase):
    cpf_check = DataFactory().find_reseller({"cpf" : purchase['cpf']})
    if not cpf_check: 
      return {"error":"reseller cpf does not exists"}

  def list_current_month_purchases(self, cpf):
    today = datetime.date.today()
    purchases = DataFactory().find_purchases_month({"cpf" : cpf}, today.month, today.year)
    total_amount = sum(p["amount"] for p in purchases)
    for p in purchases:
      p['cash_back'] = self.apply_cache_back(total_amount, p['amount'])
    return {"success" : str(purchases)}
  
  def apply_cache_back(self, total_amount, amount):
    if total_amount < 1000 :      
      amount *= 0.1
    elif total_amount <= 1500 :
        amount *= 0.15  
    else:
      amount *= 0.2 
    return amount

