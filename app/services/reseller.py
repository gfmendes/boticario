import json
import hashlib
import logging
from app.database.data_access import PurchaseDao, ResellerDao

class ResellerService():
  def add(self, reseller):
    reseller['password'] = self.__hash_password(reseller['password'])
    ResellerDao().add(reseller)
    return {"success": str(reseller)}
        
  def check_reseller_exists(self, reseller):
    email_check = ResellerDao().findOne({"email" : reseller['email']})
    if email_check: 
      return {"error":"email exists"}

    cpf_check = ResellerDao().findOne({"cpf" : reseller['cpf']})
    if cpf_check: 
      return {"error":"cpf exists"}

  def validate_password(self, login_data):
    password = self.__hash_password(login_data['password'])
    reseller = ResellerDao().findOne({"email" : login_data['email']})
    logging.warn(password)
    logging.warn(reseller)
    if (reseller and reseller['password'] == password) :
        return True
    else :
        return False
  
  def __hash_password(self, password) :
          return hashlib.sha256(password.encode('utf8')).hexdigest()

