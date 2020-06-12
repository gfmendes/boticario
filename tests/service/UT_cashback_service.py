import unittest
from app.service.cashback_service import CashbackService

class CashbackServiceTest(unittest.TestCase) :
    
    def test_get_reseller_cashback(self):
        #given
        cpf = "05134344"
        #when
        result = CashbackService().get_reseller_cashback(cpf)
        #then
        self.assertEqual(cpf*2, result)