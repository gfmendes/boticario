import json
import hashlib
import logging
from app.data.data_access import ResellerData, CashBackData

ERROR_CPF_EXISTS = {"error" : "cpf exists"}
ERROR_EMAIL_EXISTS = {"error" : "email exists"}

class ResellerService():
  def add_reseller(self, reseller):
    errors = self.__check_reseller_exists(reseller)
    if errors:
      return errors
    
    reseller['password'] = self.__hash_password(reseller['password'])
    ResellerData().add_reseller(reseller)
    return {"success": str(reseller)}
        
  def __check_reseller_exists(self, reseller):
    email_check = ResellerData().find_reseller({"email" : reseller['email']})
    if email_check: 
      return ERROR_EMAIL_EXISTS

    cpf_check = ResellerData().find_reseller({"cpf" : reseller['cpf']})
    if cpf_check: 
      return ERROR_CPF_EXISTS

  def validate_reseller_password(self, login_data):
    password = self.__hash_password(login_data['password'])
    reseller = ResellerData().find_reseller({"email" : login_data['email']})
    if (reseller and reseller['password'] == password) :
        return True
    else :
        return False

  def get_cashback_amount(self, cpf):      
    return CashBackData().get_cashback_amount(cpf)
  
  def __hash_password(self, password) :
          return hashlib.sha256(password.encode('utf8')).hexdigest()

