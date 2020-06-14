import unittest
from app.services.reseller import ResellerService

class CashBackServiceTest(unittest.TestCase) :
    
    def test_get_reseller_cashback(self):
        #given
        cpf = "05134344"
        #when
        result = ResellerService().get_cashback_amount(cpf)
        #then
        self.assertIn('credit', result)