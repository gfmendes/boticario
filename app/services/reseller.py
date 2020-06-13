import json
import hashlib
import logging
from app.dataaccess.factory import DataFactory

class ResellerService():
  def add_reseller(self, reseller):
    
    errors = self.__check_reseller_exists(reseller)
    if errors:
      return errors
    
    reseller['password'] = self.__hash_password(reseller['password'])
    DataFactory().add_reseller(reseller)
    return {"success": str(reseller)}
        
  def __check_reseller_exists(self, reseller):
    email_check = DataFactory().find_reseller({"email" : reseller['email']})
    if email_check: 
      return {"error":"email exists"}

    cpf_check = DataFactory().find_reseller({"cpf" : reseller['cpf']})
    if cpf_check: 
      return {"error":"cpf exists"}

  def validate_reseller_password(self, login_data):
    password = self.__hash_password(login_data['password'])
    reseller = DataFactory().find_reseller({"email" : login_data['email']})
    logging.warn(password)
    logging.warn(reseller)
    if (reseller and reseller['password'] == password) :
        return True
    else :
        return False

  def get_cashback_amount(self, cpf):      
    return DataFactory().get_cashback_amount(cpf)
  
  def __hash_password(self, password) :
          return hashlib.sha256(password.encode('utf8')).hexdigest()

