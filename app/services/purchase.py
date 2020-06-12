import json
import hashlib
import logging
from app.database.data_access import PurchaseDao, ResellerDao

PRE_APPROVED_RESELLERS = ['15350946056']

class PurchaseService():
  def add(self, purchase):
    logging.warn("Adding new purchase request %s" % purchase)
    purchase['status'] = 'Approved' if purchase['cpf'] in PRE_APPROVED_RESELLERS else 'Validating'
    purchase = PurchaseDao().add(purchase)
    return {"success": str(purchase)}

  def validate_purchase(self, purchase):
    cpf_check = ResellerDao().findOne({"cpf" : purchase['cpf']})
    if not cpf_check: 
      return {"error":"reseller cpf does not exists"}

  def list(self, cpf):
    print(PurchaseDao().find({"cpf" : cpf}))
    return {"success" : ""}
