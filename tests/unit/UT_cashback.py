import unittest
from app.services.cashback import CashBackService

class CashBackServiceTest(unittest.TestCase) :
    
    def test_get_reseller_cashback(self):
        #given
        cpf = "05134344"
        #when
        result = CashBackService().get_reseller_cashback(cpf)
        #then
        self.assertEqual(cpf*2, result)