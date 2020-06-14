import logging
import datetime
from app.data.data_access import ResellerData, PurchaseData

PRE_APPROVED_RESELLERS = ['15350946056'] #This data should be externalized in an API call or database

class PurchaseService():
  def add_purchase(self, purchase):
    errors = self.__validate_purchase(purchase)
    if errors : return errors

    purchase['status'] = 'Approved' if purchase['cpf'] in PRE_APPROVED_RESELLERS else 'Validating'
    return PurchaseData().add_purchase(purchase)
    
  def __validate_purchase(self, purchase):
    cpf_check = ResellerData().find_reseller({"cpf" : purchase['cpf']})
    if not cpf_check: 
      return {'error':'reseller cpf does not exists'}

  def list_current_month_purchases(self, cpf):
    today = datetime.date.today()
    purchases = PurchaseData().find_monthly_purchases({"cpf" : cpf, "month" : today.month, "year" : today.year})
    total_amount = sum(p["amount"] for p in purchases)
    for p in purchases: 
      p['cash_back'] = self.__apply_cache_back(total_amount, p['amount'])
    return purchases
  
  def __apply_cache_back(self, total_amount, amount):
    if total_amount <= 1000 : return amount * 0.1
    elif total_amount <= 1500 : return amount * 0.15  
    else: return amount * 0.2 

