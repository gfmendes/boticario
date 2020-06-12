import json
import hashlib
import logging
from app.database.data_access import PurchaseDao, ResellerDao

class CashBackService():
    def get_reseller_cashback(self, cpf):      
        return cpf*2